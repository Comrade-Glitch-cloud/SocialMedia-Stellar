from django.urls import path
from .views import DockUp, cadetprofile, cadetdetails
from django.contrib.auth import views as auth_views

app_name = 'star_accounts_hub'

urlpatterns = [
    path('dockup/', DockUp.as_view(), name='dockup'),
    path('cadetprofile/', cadetprofile, name='cadetprofile'),
    path('cadetdetails/', cadetdetails, name='cadetdetails'),
    path('dockin/', auth_views.LoginView.as_view(template_name='star_accounts_hub/dockin.html'), name='dockin'),
    path('dockout/', auth_views.LogoutView.as_view(next_page='home'), name='dockout'),
]
