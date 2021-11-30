# function to put-together templates depending on the browser request
from django.shortcuts import render 

# other imports that may be useful
from django.utils import timezone 
from django.shortcuts import get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect

def index(request):
    return render(request, 'blog/index.html')