from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm

# Create your views here.

def home(request):
    posts = Post.objects.all()
    return render(request, 'blog/home.html', {'posts': posts})

def new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            if not form.data['author']:
                post.author = request.user
            post.save()
        return redirect('/'+str(post.id))
    else:
        form = PostForm()
        return render(request, 'blog/new.html', {'form': form})

def show(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'blog/show.html', {'post': post})

def delete(request, post_id):
    post = Post.objects.filter(pk=post_id)
    post.delete()
    return redirect('home')

def edit(request, id):
    post = get_object_or_404(Post, pk=id)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            if not form.data['author']:
                post.author = request.user
            post.save()
        return redirect('show', post_id=post.pk)
    else:
        form = PostForm(instance=post)
        return render(request, 'blog/edit.html', {'form': form, 'post': post})