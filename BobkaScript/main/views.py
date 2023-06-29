from django.shortcuts import render
from .models import *

def main_page(request):
    return render(request, 'main/main_page.html')


def docs(request):
    return render(request, 'main/docs.html')


def about(request):
    posts = Post.objects.all()
    return render(request, 'main/about.html', {'posts': False})


def secret(request):
    posts = Post.objects.all()
    return render(request, 'main/about.html', {'posts': posts})
