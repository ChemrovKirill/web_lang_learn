from django.shortcuts import render
from django.core.cache import cache
from . import vocabulary_db

def index(request):
    return render(request, "index.html")

def vocabulary(request):
    voc_items = vocabulary_db.get_items_for_table()
    return render(request, "vocabulary.html", context={"voc_items": voc_items})