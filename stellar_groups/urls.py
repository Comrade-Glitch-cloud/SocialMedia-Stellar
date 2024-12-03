from django.urls import path
from . import views

app_name = 'stellar_groups'

urlpatterns = [
    path('', views.ListStellarGroups.as_view(), name='all'),
    path('new/', views.CreateStellarGroup.as_view(), name='create'),
    path('posts/in/<slug:slug>/', views.SingleStellarGroup.as_view(), name='single'),
    path('join/<slug:slug>/', views.JoinStellarGroup.as_view(), name='join'),
    path('leave/<slug:slug>/', views.LeaveStellarGroup.as_view(), name='leave'),
]
