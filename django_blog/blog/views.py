from django.http import HttpResponse
from django.shortcuts import render

from django.urls import include, path

# Create your views here.
def home(rquest):
    return HttpResponse("Welcome to my blog")
