from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from .views import HomePage, TestPage, ThanksPage, finder

urlpatterns = [
    path('admin/', admin.site.urls),                              # Admin panel
    path('', HomePage.as_view(), name='home'),                    # Home page
    path('accounts/', include('django.contrib.auth.urls')),       # Authentication URLs
    path('star_accounts_hub/', include('star_accounts_hub.urls')),  # User accounts
    path('stellar_posts/', include('stellar_posts.urls')),        # Posts
    path('stellar_groups/', include('stellar_groups.urls')),      # Groups
    path('stellarsearch/', finder, name='stellarsearch'),         # Stellar search functionality
    path('test/', TestPage.as_view(), name='test'),               # Test page
    path('thanks/', ThanksPage.as_view(), name='thanks'),         # Thanks page
]

# Add media URLs for development mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
