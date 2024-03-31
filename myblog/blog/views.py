from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post, Comment
import time

# Create your views here.
def home(request):
    posts = Post.objects.all()

    context = {
        'posts': posts,
    }

    return render(request, 'index.html', context)


def aboutme(request):
    return render(request, 'aboutme.html')


def new_comment(request):
    text = request.GET['text']
    post_id = request.GET['post_id']
    comment = Comment(post_id=post_id, text=text)
    comment.save()
    return redirect('/')