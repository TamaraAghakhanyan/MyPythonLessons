from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def home(rquest):
    return HttpResponse("Welcome to my blog")
