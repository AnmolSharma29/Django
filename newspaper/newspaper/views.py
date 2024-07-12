from django.http import HttpResponse
from django.shortcuts import render
from headlines.models import Headlines
from top_news.models import topNews


def homePage(request):
    headlineData = Headlines.objects.all()
    topNewsData = topNews.objects.all()
    data={
        'headlineData':headlineData,
        'topNewsData':topNewsData,
    }
    return render(request,"home.html",data)

def top_news(request,id):
    headlineData = Headlines.objects.all()
    topNewsData = topNews.objects.order_by('topNews_date').get(id=id)
    return render(request,'base.html',{
        'headlineData':headlineData,
        'topNewsData':topNewsData
    })

def base(request):
    headlineData = Headlines.objects.all()
    topNewsData = topNews.objects.all()
    data={
        'headlineData':headlineData,
        'topNewsData':topNewsData,
    }
    return render(request,"base.html",data)
