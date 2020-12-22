from django.shortcuts import render
from django.http import HttpResponse


def index(response):
    return HttpResponse("<h1> hiiiii </h1>")


def v1(response):
    return HttpResponse("v111")

# Create your views here.
