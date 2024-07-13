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

def top_news(request,id):
    headlineData = Headlines.objects.all()
    topNewsData = topNews.objects.get(id=id)
    return render(request,'base.html',{
        'headlineData':headlineData,
        'topNewsData':topNewsData
    })

def sportsPage(request,id):
    headlineData = Headlines.objects.all()
    sportData = Sports.objects.get(id=id)
    return render(request,'sports.html',{
        'headlineData':headlineData,
        'sportData':sportData
    })
def editorialPage(request,id):
    headlineData = Headlines.objects.all()
    editorialData = Editorial.objects.get(id=id)
    return render(request,'editorial.html',{
        'headlineData':headlineData,
        'editorialData':editorialData
    })
