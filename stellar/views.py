from django.views.generic import TemplateView
from django.shortcuts import render
from django.db.models import Q
from stellar_posts.models import StellarPost
from stellar_groups.models import StellarGroup

class HomePage(TemplateView):
    template_name = 'index.html'

class TestPage(TemplateView):
    template_name = 'test.html'

class ThanksPage(TemplateView):
    template_name = 'thanks.html'

def finder(request):
    query = request.GET.get('query')
    if query:
        posts = StellarPost.objects.filter(Q(message__icontains=query))
        groups = StellarGroup.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )
    else:
        posts = StellarPost.objects.all()
        groups = StellarGroup.objects.all()

    context = {
        'posts': posts,
        'groups': groups,
        'query': query,
    }
    return render(request, 'finder.html', context)
