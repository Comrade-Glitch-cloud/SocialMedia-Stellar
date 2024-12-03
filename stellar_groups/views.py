from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, RedirectView
from .models import StellarGroup, StellarGroupMember
from django.urls import reverse
from django.db import IntegrityError
from django.contrib import messages

class ListStellarGroups(ListView):
    model = StellarGroup
    template_name = 'stellar_groups/group_list.html'

class CreateStellarGroup(CreateView):
    model = StellarGroup
    fields = ['name', 'description']
    template_name = 'stellar_groups/group_form.html'

class SingleStellarGroup(DetailView):
    model = StellarGroup
    template_name = 'stellar_groups/group_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['group'] = get_object_or_404(StellarGroup, slug=self.kwargs.get('slug'))
        return context

class JoinStellarGroup(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse('stellar_groups:single', kwargs={'slug': self.kwargs.get('slug')})

    def get(self, request, *args, **kwargs):
        group = get_object_or_404(StellarGroup, slug=self.kwargs.get('slug'))
        try:
            StellarGroupMember.objects.create(user=self.request.user, group=group)
        except IntegrityError:
            messages.warning(self.request, 'Warning: already a member of stellar!')
        else:
            messages.success(self.request, 'You are one of us now!')
        return super().get(request, *args, **kwargs)

class LeaveStellarGroup(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse('stellar_groups:single', kwargs={'slug': self.kwargs.get('slug')})

    def get(self, request, *args, **kwargs):
        try:
            membership = StellarGroupMember.objects.filter(
                user=self.request.user,
                group__slug=self.kwargs.get('slug')
            ).get()
        except StellarGroupMember.DoesNotExist:
            messages.warning(self.request, 'Sorry, you are not in this group!')
        else:
            membership.delete()
            messages.success(self.request, 'You have left the group!')
        return super().get(request, *args, **kwargs)
