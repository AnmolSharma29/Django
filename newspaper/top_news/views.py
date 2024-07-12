from django.shortcuts import render
from django.views.generic import ListView, DetailView
from top_news.models import topNews
class NewsListView(ListView):
    model = topNews
    template_name = 'home.html'
class NewsDetailView(DetailView):
    model = topNews
    template_name = 'base.html'

# Create your views here.
