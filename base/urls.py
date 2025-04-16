from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('posts/', views.POSTS, name='posts'),
    path('post/<str:pk>/', views.POST, name='post'),
    path('profile/', views.Profile, name='profile'),
    path('main/', views.main, name='main'), 
    path('create-post/', views.create_post, name='create_post'),
    path('update-post/<str:pk>/', views.update_post, name='update_post'),
    path('delete-post/<str:pk>/', views.delete_post, name='delete_post'),
    
    path('send-email/', views.send_email, name='send_email'),
]
