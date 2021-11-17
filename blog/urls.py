from django.urls import path
from . import views

urlpatterns = [
    # Landing page path (the empty path '' redirects to the views.post_list module) is a list of posts
    # What do we want the landing page to be for Colorado Family Insurance?
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]