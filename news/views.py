#-*- coding: utf-8 -*-
from django.shortcuts import render
from news.models import News

def home(request):
    articles = News.objects.all()
    return render(request, 'news/index.html', {'articles':articles})
