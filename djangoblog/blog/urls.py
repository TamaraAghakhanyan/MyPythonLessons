from django.contrib import admin
# blog/urls.py

from django.urls import path
from blog.views import Home, Article



urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('article', Article.as_view())
]