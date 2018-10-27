from django.shortcuts import render, get_object_or_404
from .models import Blog


def home(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/home.html', {'blogs':blogs})

def allblogs(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/allblogs.html', {'blogs':blogs})

def detail(request, blog_id):
    detailblog = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'blog/detail.html', {'blog':detailblog})

def blog1(request):
    return render(request, 'blog/blog1.html')