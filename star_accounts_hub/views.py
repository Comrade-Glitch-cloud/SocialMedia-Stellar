from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import CadetProfile
from django.contrib.auth.models import User

class DockUp(CreateView):
    model = User
    fields = ['username', 'first_name', 'last_name', 'email', 'password']
    success_url = reverse_lazy('star_accounts_hub:dockin')
    template_name = 'star_accounts_hub/dockup.html'

@login_required
def cadetprofile(request):
    if not hasattr(request.user, 'cadet'):
        if not CadetProfile.objects.filter(user=request.user).exists():
            CadetProfile.objects.create(user=request.user, stellarname=request.user.username)

    if request.method == 'POST':
        stellarname = request.POST.get('stellarname')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        cadet_picture = request.FILES.get('cadet_picture')

        request.user.cadet.stellarname = stellarname
        request.user.email = email
        request.user.first_name = first_name
        request.user.last_name = last_name
        if cadet_picture:
            request.user.cadet.cadet_picture = cadet_picture
        request.user.cadet.save()
        request.user.save()

        return redirect('star_accounts_hub:cadetdetails')

    cadet_profile = CadetProfile.objects.get(user=request.user)
    context = {'cadet': cadet_profile}
    return render(request, 'star_accounts_hub/cadetprofile.html', context)

@login_required
def cadetdetails(request):
    if not hasattr(request.user, 'cadet'):
        if not CadetProfile.objects.filter(user=request.user).exists():
            CadetProfile.objects.create(user=request.user, stellarname=request.user.username)
    user_cadet = request.user.cadet
    return render(request, 'star_accounts_hub/cadetdetails.html', {'cadet': user_cadet})
