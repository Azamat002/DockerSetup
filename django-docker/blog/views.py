# from django.shortcuts import render
# from .models import Post
#
# def post_list(request):
#     posts = Post.objects.all()
#     return render(request, 'blog/post_list.html', {'posts': posts})

# C:\Users\Acer\Documents\A - KBTU\WEB\Azamat-Ex3\django-docker\blog\views.py

from django.shortcuts import render

def post_list(request):
    return render(request, 'blog/post_list.html')  # Make sure to create this template
