from django.contrib import admin
# blog/urls.py

from django.urls import path
from .views import Home

# urlpatterns = [
#     path('', home, name='home'),  # Define the URL pattern for the home view
# ]

urlpatterns = [
    path('', Home.as_view)
]