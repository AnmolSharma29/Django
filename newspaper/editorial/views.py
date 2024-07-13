from django.shortcuts import render
from django.views.generic import ListView, DetailView
from editorial.models import Editorial
class EditorialListView(ListView):
    model = Editorial
    template_name = 'home.html'
class EditorialDetailView(DetailView):
    model = Editorial
    template_name = 'editorial.html'
# Create your views here.

