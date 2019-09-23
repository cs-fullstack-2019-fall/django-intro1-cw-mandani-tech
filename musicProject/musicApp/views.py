from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def music(request):
    return HttpResponse("Hello Welcome to My Music Page")


def shreyaFunction(request):
    return HttpResponse("Shreya is my First Favorite Artist")


def rehmanFunction(request):
    return HttpResponse("Shreya is my First Favorite Artist")


def alkaFunction(request):
    return HttpResponse("Shreya is my First Favorite Artist")
