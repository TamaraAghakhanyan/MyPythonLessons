from django.contrib import admin
# blog/urls.py

from django.urls import path
from blog.views import home  # Import the home view

urlpatterns = [
    path('', home, name='home'),  # Define the URL pattern for the home view
]
