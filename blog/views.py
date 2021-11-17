from django.shortcuts import render # function to put-together templates
from .models import Post # include the Post model to pull data
from django.utils import timezone 
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect

def post_list(request):
    """
    Generate a list of posts.
    """
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    # render() provides post_list.html with the list of posts as posts
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    """
    Get the requested post.
    Render using the post_detail template.
    """
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    """
    Create a new post.
    """
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:    
        form = PostForm()

    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})