from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.decorators.http import require_http_methods
from .models import CadetProfile
from django.contrib.auth.models import User

class DockUp(CreateView):
    model = User
    fields = ['username', 'first_name', 'last_name', 'email', 'password']
    success_url = reverse_lazy('star_accounts_hub:dockin')
    template_name = 'star_accounts_hub/dockup.html'

@login_required
@require_http_methods(["GET", "POST"])
def cadetprofile(request):
    # Ensure cadet profile exists for the user
    cadet_profile, created = CadetProfile.objects.get_or_create(user=request.user, defaults={'stellarname': request.user.username})

    if request.method == 'POST':
        cadet_profile.stellarname = request.POST.get('stellarname')
        request.user.email = request.POST.get('email')
        request.user.first_name = request.POST.get('first_name')
        request.user.last_name = request.POST.get('last_name')
        cadet_picture = request.FILES.get('cadet_picture')

        if cadet_picture:
            cadet_profile.cadet_picture = cadet_picture

        cadet_profile.save()
        request.user.save()

        return redirect('star_accounts_hub:cadetdetails')

    context = {'cadet': cadet_profile}
    return render(request, 'star_accounts_hub/cadetprofile.html', context)

@login_required
@require_http_methods(["GET"])
def cadetdetails(request):
    # Ensure cadet profile exists for the user
    cadet_profile, created = CadetProfile.objects.get_or_create(user=request.user, defaults={'stellarname': request.user.username})

    return render(request, 'star_accounts_hub/cadetdetails.html', {'cadet': cadet_profile})
