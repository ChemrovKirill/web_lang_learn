from django.shortcuts import render
from django.core.cache import cache

def index(request):
    return render(request, "index.html")