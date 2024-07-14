from django.http import HttpResponse
from django.shortcuts import render
from headlines.models import Headlines
from top_news.models import topNews
from sports.models import Sports
from editorial.models import Editorial

def homePage(request):
    headlineData = Headlines.objects.all()
    topNewsData = topNews.objects.order_by('-id').all()
    sportData = Sports.objects.order_by('-id').all()
    editorialData = Editorial.objects.order_by('-id').all()
    data={
        'headlineData':headlineData,
        'topNewsData':topNewsData,
        'sportData':sportData,
        'editorialData':editorialData
    }
    return render(request,"home.html",data)

def top_news(request,slug):
    headlineData = Headlines.objects.all()
    topNewsData = topNews.objects.get(slug=slug)
    return render(request,'base.html',{
        'headlineData':headlineData,
        'topNewsData':topNewsData
    })

def sportsPage(request,slug):
    headlineData = Headlines.objects.all()
    sportData = Sports.objects.get(sports_slug=slug)
    return render(request,'sports.html',{
        'headlineData':headlineData,
        'sportData':sportData
    })
def editorialPage(request,slug):
    headlineData = Headlines.objects.all()
    editorialData = Editorial.objects.get(editorial_slug=slug)
    return render(request,'editorial.html',{
        'headlineData':headlineData,
        'editorialData':editorialData
    })
