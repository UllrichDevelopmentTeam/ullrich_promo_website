from django.urls import path
from . import views

urlpatterns = [
    # Landing page path (the empty path '' redirects to the views.post_list module) is a list of posts
    # What do we want the landing page to be for Colorado Family Insurance?
    path('', views.index, name='index'),
]