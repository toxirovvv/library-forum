from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='add_post_home'),
    path('create-post/', views.CreatePost.as_view(), name='create_post'),
    path('like/<int:pk>', views.post_like, name='like_post'),
    path('post/<int:pk>', views.single_post, name='single'),
    path('comment/', views.comment, name='comment'),
    path('search/', views.search, name="search"),
    path('my-likes/', views.my_likes, name='my_likes')
]    