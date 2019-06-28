from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post, Follow, Follow_post
from .forms import PostForm, CommentForm

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
    form = CommentForm()
    follow = Follow_post.objects.filter(post=post)
    return render(request, 'blog/show.html', {'post': post, 'form':form, 'follow':follow})

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

def commentcreate(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        if not form.data['author']:
            post.author = request.user
        comment.save()
    return redirect('show', post_id=post.pk)

def postfollow(request, id):
    post = get_object_or_404(Post, pk=id)
    follow = Follow(follow = True)
    follow.save()
    fw = Follow_post(
        follow = follow,
        post = post,
        author = request.user
        )
    fw.save()
    return redirect('show', post_id=post.pk)