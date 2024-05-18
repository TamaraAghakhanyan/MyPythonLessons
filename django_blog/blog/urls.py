from django.contrib import admin
from django.urls import include, path
from blog.views import home


urlpatterns = [
    path('', home)
]