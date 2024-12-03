from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CadetSignUpForm, CadetUpdateForm
from .models import CadetProfile

class DockUp(CreateView):
    form_class = CadetSignUpForm
    success_url = reverse_lazy('star_accounts_hub:dockin')
    template_name = 'star_accounts_hub/dockup.html'

@login_required
def cadetprofile(request):
    if not hasattr(request.user, 'cadet'):
        if not CadetProfile.objects.filter(user=request.user).exists():
            CadetProfile.objects.create(user=request.user, stellarname=request.user.username)

    if request.method == 'POST':
        cadet_form = CadetUpdateForm(request.POST, request.FILES, instance=request.user.cadet)
        if cadet_form.is_valid():
            cadet_form.save()
            return redirect('star_accounts_hub:cadetdetails')
    else:
        cadet_form = CadetUpdateForm(instance=request.user.cadet)

    return render(request, 'star_accounts_hub/cadetprofile.html', {'cadet_form': cadet_form, 'cadet': request.user.cadet})

@login_required
def cadetdetails(request):
    if not hasattr(request.user, 'cadet'):
        if not CadetProfile.objects.filter(user=request.user).exists():
            CadetProfile.objects.create(user=request.user, stellarname=request.user.username)
    user_cadet = request.user.cadet
    return render(request, 'star_accounts_hub/cadetdetails.html', {'cadet': user_cadet})
