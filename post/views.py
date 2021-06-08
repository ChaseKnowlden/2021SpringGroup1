from django.http import response
from django.http.response import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from . import routes
from .models import Post
from person.models import Person
import json
import requests
import random
# Create your views here.
news_api = "8bf9d2e3fc0f43dd9af74470803d6384"


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
        if "id" in request.session:
            post.posterid = request.session["id"]
        elif "id" in request.GET:
            post.posterid = request.GET["id"]
        else:
            return HttpResponse("You need to be logged in to the system or provide a user id!")
        post.title = title
        post.description = description
        post.likeNum = 0
        post.save()
    return HttpResponseRedirect("..")


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
        likerId = request.session["id"]
        likers = post.likedBy
        if len(likers) == 2:
            post.likeNum = 1
            post.likedBy = '[' + str(likerId) + ']'
        elif ',' not in likers:
            likee = likers[1:-1]
            if likee == str(likerId):
                post.likeNum = 0
                post.likedBy = '[]'
            else:
                post.likeNum = 2
                post.likedBy = likers[0:-1] + ',' + str(likerId) + ']'
        else:
            allLikers = likers[1:-1].split(',')
            alreadyin = False
            for item in allLikers:
                if str(likerId) == str(item):
                    alreadyin = True
                    break
            if alreadyin:
                allLikers.remove(str(likerId))
                post.likeNum -= 1
                if len(allLikers) == 1:
                    post.likedBy = '[' + str(allLikers[0]) + ']'
                else:
                    post.likedBy = '[' + ','.join(allLikers) + ']'
            else:
                allLikers.append(str(likerId))
                post.likeNum += 1
                post.likedBy = '[' + ','.join(allLikers) + ']'

        post.save()
        return HttpResponseRedirect("/post/viewPost")

    return HttpResponseRedirect("/post/viewPost")


def createDummyPost(request):
    newsresponse = requests.get(
        "https://newsapi.org/v2/top-headlines?country=tr&pageSize=35&apiKey=" + news_api)
    value = newsresponse.json()
    size = value["totalResults"]
    randomNew = random.randint(1, size-1)
    article = value["articles"][randomNew]

    title = article["title"]
    description = article["description"]
    post = Post()
    if "id" in request.session:
        post.posterid = request.session["id"]
    elif "id" in request.GET:
        post.posterid = request.GET["id"]
    else:
        return HttpResponse("You need to be logged in to the system or provide a user id!")

    post.title = title
    post.description = description
    post.likeNum = 0
    post.save()
    # value["articles"][randomNew]
    return HttpResponse("Your post with title: {0} and description: {1} is created succesfully!".format(title, description))
