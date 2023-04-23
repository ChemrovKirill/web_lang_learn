from django.shortcuts import render
from django.core.cache import cache
from . import vocabulary_db, cards_db

def index(request):
    return render(request, "index.html")

def vocabulary(request):
    voc_items = vocabulary_db.get_items_for_table()
    return render(request, "vocabulary.html", context={"voc_items": voc_items})

def add_word(request):
    return render(request, "add_word.html")

def add_word_post(request):
    if request.method == "POST":
        cache.clear()
        item = {"word":request.POST.get("word"),
                "ru_translate":request.POST.get("ru_translate"),
                "definition":request.POST.get("definition"),
                "example":request.POST.get("example", ""),
                "comment":request.POST.get("comment", ""),
                }
        context = {}
        if len(item["word"]) == 0:
            context["success"] = False
            context["comment"] = "You didn't enter a word."
        elif len(item["ru_translate"]) == 0:
            context["success"] = False
            context["comment"] = "You didn't enter a translation."
        elif len(item["definition"]) == 0:
            context["success"] = False
            context["comment"] = "You didn't enter a definition."
        elif vocabulary_db.in_db(item["word"]):
            context["success"] = False
            context["comment"] = f"The word \'{item['word']}\' is already in the vocabulary."
        else:
            context["success"] = True
            context["comment"] = "The word has been added."
            vocabulary_db.add_word(item)
        return render(request, "add_word_post.html", context)
    else:
        add_word(request)

def create_cards(request):
    context = {}
    items_for_cards = vocabulary_db.get_rnd_cards(10)
    cards_db.set_cards(items_for_cards)
    cur_card = cards_db.get(1)
    context = {"num_cards":len(items_for_cards),
               "current_card":1,
               "current_side":"front",
               "front_text":cur_card.word,
               "front_subtext":"",
               "back_text":cur_card.ru_translate,
               "back_subtext":cur_card.definition,
              }
    return render(request, "cards.html", context)