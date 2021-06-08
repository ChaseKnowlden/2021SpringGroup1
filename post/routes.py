from django.conf.urls import url
from django.urls import path
from django.contrib import admin
from . import views
app_name = "postroutes"

urlpatterns = [
    path("", views.mainPage, name="mainpage"),
    path("createPost/", views.createPost, name="createpost"),
    path("viewPost/", views.viewPost, name="viewpost"),
    path("savePost", views.savePost, name="savepost"),
    path("likePost", views.likePost, name="likepost"),
    path("createDummyPost", views.createDummyPost, name="createdummypost"),
]
