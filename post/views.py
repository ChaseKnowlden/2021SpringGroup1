from django.http.response import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from . import routes
from .models import Post
from person.models import Person
import json
# Create your views here.


def mainPage(request):
    if request.method == "POST":
        if request.POST["post"] == "logout":
            request.session.flush()
            return HttpResponseRedirect("../")
    return render(request, "post/mainPage.html", {"personfirst": request.session["firstname"], "personlast": request.session["lastname"]})


def createPost(request):
    return render(request, "post/createPost.html", {"personfirst": request.session["firstname"], "personlast": request.session["lastname"]})


def savePost(request):
    if request.method == "POST":
        title = request.POST["title"]
        description = request.POST["description"]
        post = Post()
        post.posterid = request.session["id"]
        post.title = title
        post.description = description
        post.likeNum = 0
        post.save()
    else:
        title = request.GET["title"]
        description = request.GET["description"]
        post = Post()
        post.posterid = request.GET["id"]
        post.title = title
        post.description = description
        post.likeNum = 0
        post.save()
    return HttpResponseRedirect("/post")


def viewPost(request):
    posts = Post.objects.all()
    if request.method == "GET":

        if "type" in request.GET:
            if "id" in request.GET:
                postid = request.GET["id"]
                post = Post.objects.filter(id=postid)
                return HttpResponse(JsonResponse(post[0].__str__()))
            allposts = {"post": []}
            for item in posts:
                post = item.__str__()
                allposts["post"].append(post)
            return HttpResponse(JsonResponse(allposts))

        return render(request, "post/viewPosts.html", {"personfirst": request.session["firstname"], "personlast": request.session["lastname"], "allposts": Post.objects.all()})
    if request.method == "POST":
        print(request.POST["like"])
        return render(request, "post/viewPosts.html", {"personfirst": request.session["firstname"], "personlast": request.session["lastname"], "allposts": Post.objects.all()})


def likePost(request):
    if request.method == "POST":
        postid = request.POST["like"]
        post = Post.objects.get(id=postid)
        post.likeNum = post.likeNum + 1
        post.save()
        return HttpResponseRedirect("/post/viewPost")

    return HttpResponseRedirect("/post/viewPost")
