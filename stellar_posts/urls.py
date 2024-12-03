from django.urls import path
from . import views

app_name = 'stellar_posts'

urlpatterns = [
    path('', views.StellarPostList.as_view(), name='all'),
    path('new/', views.CreateStellarPost.as_view(), name='create'),
    path('by/<str:username>/', views.UserStellarPosts.as_view(), name='for_user'),
    path('by/<str:username>/<int:pk>/', views.StellarPostDetail.as_view(), name='single'),
    path('delete/<int:pk>/', views.DeleteStellarPost.as_view(), name='delete'),
]
