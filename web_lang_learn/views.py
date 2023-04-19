from django.shortcuts import render
from django.core.cache import cache
from . import vocabulary_db

def index(request):
    return render(request, "index.html")

def vocabulary(request):
    voc_items = vocabulary_db.get_items_for_table()
    return render(request, "vocabulary.html", context={"voc_items": voc_items})

def add_word(request):
    return render(request, "add_word.html")

def add_word_post(voc_item):
    if request.method == "POST":
        cache.clear()
        item.word = request.POST.get("word")
        item.ru_translate = request.POST.get("ru_translate")
        item.definition = request.POST.get("definition")
        item.example = request.POST.get("example", "")
        item.comment = request.POST.get("comment", "")
        context = {"user": user_name}
        if len(item.word) == 0:
            context["success"] = False
            context["comment"] = "You didn't enter a word"
        elif len(item.ru_translate) == 0:
            context["success"] = False
            context["comment"] = "You didn't enter a translation"
        elif len(item.definition) == 0:
            context["success"] = False
            context["comment"] = "You didn't enter a definition"
        else:
            context["success"] = True
            context["comment"] = "The word has been added"
            vocabulary_db.add_word(item)
        if context["success"]:
            context["success-title"] = ""
        return render(request, "add_word_request.html", context)
    else:
        add_word(request)

