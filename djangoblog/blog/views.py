from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from datetime import datetime
from django.shortcuts import render
from blog.models import ArticleModel
from django.utils import timezone



class Home(View):
    def get(self,request):
        return HttpResponse('Welcome to my blog :)')
    def post(self,request):
        return HttpResponse('[POST] Welcome to my blog :)')


class Article(View):
    def get(self, request):
        articles = ArticleModel.objects.all()
        return render(request, "articles.html", {"articles": articles})

    def post(self, request):
        title = request.POST["title"]
        category = request.POST["category"]
        author = request.POST["content"]
        content = request.POST["content"]

        ArticleModel.objects.create(title=title, category=category, author= author, content= content, created_at= datetime.now(tz=timezne.utc))