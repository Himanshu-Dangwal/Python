from django.shortcuts import render
from django.http import HttpResponse
from . import models

# Create your views here.
def post(request):
    posts = models.Post.objects.all()
    return render(request, "posts/posts_list.html",{'postss': posts})

# def post_list(request,slug):
#     return HttpResponse(slug)

def post_list(request,slug):
    post = models.Post.objects.get(slug=slug)
    return render(request,"posts/post_page.html",{'post':post})
