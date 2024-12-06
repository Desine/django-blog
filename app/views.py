from django.shortcuts import render, redirect
from .models import Post
from django.http import HttpResponse
from .forms import PostForm


def home(request):
    posts = Post.objects.all()
    return render(request, "home.html", {"posts": posts})

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'post.html', {'post': post})

def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
                
        if form.is_valid():
            form.save()
            return redirect('app:home')
            
    else:
        form = PostForm()
    
    print(request.method)
    
    return render(request, 'post_create.html', {'form': form})

def post_delete(request, pk):
    post = Post.objects.get(pk=pk)

    if request.method == 'POST':
        post.delete()
        return redirect('app:home')

    return render(request, 'post_delete.html', {'post': post})
