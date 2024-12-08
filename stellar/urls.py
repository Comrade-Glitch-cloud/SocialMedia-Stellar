from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from .views import HomePage, TestPage, ThanksPage, finder

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePage.as_view(), name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('star_accounts_hub/', include('star_accounts_hub.urls')),
    path('stellar_posts/', include('stellar_posts.urls')),
    path('stellar_groups/', include('stellar_groups.urls')),
    path('stellarsearch/', finder, name='stellarsearch'),
    path('test/', TestPage.as_view(), name='test'),
    path('thanks/', ThanksPage.as_view(), name='thanks'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
