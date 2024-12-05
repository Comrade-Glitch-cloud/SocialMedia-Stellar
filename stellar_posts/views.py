from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from braces.views import SelectRelatedMixin
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin  # Import this mixin
from .models import StellarPost
from django.contrib import messages
from django.http import Http404

User = get_user_model()

class StellarPostList(SelectRelatedMixin, generic.ListView):
    model = StellarPost
    select_related = ('user', 'group')
    template_name = 'stellar_posts/post_list.html'

class UserStellarPosts(generic.ListView):
    model = StellarPost
    template_name = 'stellar_posts/user_post_list.html'

    def get_queryset(self):
        try:
            self.post_user = User.objects.prefetch_related('posts').get(username__iexact=self.kwargs.get('username'))
        except User.DoesNotExist:
            raise Http404
        else:
            return self.post_user.posts.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_user'] = self.post_user
        return context


class StellarPostDetail(SelectRelatedMixin, generic.DetailView):
    model = StellarPost
    select_related = ('user', 'group')
    template_name = 'stellar_posts/post_detail.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user__username__iexact=self.kwargs.get('username'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post'] = self.get_object()
        return context

class CreateStellarPost(LoginRequiredMixin, SelectRelatedMixin, generic.CreateView):
    fields = ('message', 'group')
    model = StellarPost
    template_name = 'stellar_posts/post_form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return self.render_to_response(self.get_context_data(form=self.get_form_class()()))


class DeleteStellarPost(LoginRequiredMixin, SelectRelatedMixin, generic.DeleteView):
    model = StellarPost
    select_related = ('user', 'group')
    success_url = reverse_lazy('stellar_posts:all')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_id=self.request.user.id)

    def delete(self, *args, **kwargs):
        messages.success(self.request, 'Post Deleted')
        return super().delete(*args, **kwargs)
