from django.shortcuts import render
from django.views.generic import ListView, DetailView
from sports.models import Sports
class SportsListView(ListView):
    model = Sports
    template_name = 'home.html'
class SportsDetailView(DetailView):
    model = Sports
    template_name = 'sports.html'
# Create your views here.
