from django import forms
from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import *

@user_passes_test(lambda user:user.is_authenticated)
def blog_index(request):
    posts = Post.objects.all().order_by('-created_on')
    context = {
        'posts':posts
    }
    return render(request, 'blog_index.html', context)

@login_required
def blog_category(request, category):
    posts = Post.objects.filter(category__name__contains=category)
    context = {
        'posts':posts,
        'category':category
    }

    return render(request, 'blog_category.html', context)

@login_required
def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)
    
    if request.method == 'POST':
        author = request.POST['author']
        body = request.POST['comment'].capitalize()
        comment = Comment(author=author, body=body, post=post)
        comment.save()

    comments = Comment.objects.filter(post=post)
    context = {
        'post':post,
        'comments':comments
    }

    return render(request, 'blog_detail.html', context)
    


