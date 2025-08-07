from django.urls import path 
from . import views

urlpatterns = [
    path('',views.post, name="posts"),
    path('<slug:slug>',views.post_list,name="postlist")
]