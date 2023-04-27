from django.shortcuts import render
from django.core.cache import cache
from . import vocabulary_db, cards_db


def index(request):
    """
    renders the main page, put 3 random words
    with definition for carousel in the context
    """
    voc_items = vocabulary_db.get_rnd_items(3)
    context = {}
    for i, item in enumerate(voc_items):
        context[f"word_{i+1}"] = item.word
        context[f"definition_{i+1}"] = item.definition
    return render(request, "index.html", context)


def vocabulary(request):
    """
    renders the page with vocabulary table,
    puts all the words from the vocabulary database in the context
    """
    voc_items = vocabulary_db.get_items_for_table()
    return render(request, "vocabulary.html", context={"voc_items": voc_items})


def add_word(request):
    """ renders the word adding page """
    return render(request, "add_word.html")


def add_word_post(request):
    """
    add the word data from post request to the database
    and renders the page of success/error
    """
    if request.method == "POST":
        cache.clear()
        item = {"word": request.POST.get("word"),
                "ru_translate": request.POST.get("ru_translate"),
                "definition": request.POST.get("definition"),
                "example": request.POST.get("example", ""),
                "comment": request.POST.get("comment", ""),
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
    return add_word(request)


def create_cards(request):
    """ renders the cards creating page """
    return render(request, "create_cards.html")


def cards(request):
    """
    renders the page with cards for the first time (POST)
    and when switching the cards (GET)
    """
    if request.method == "POST":
        cache.clear()
        num_cards = int(request.POST.get("num_cards"))
        mode = request.POST.get("mode")
        is_example = request.POST.get("is_example")
        is_definition = request.POST.get("is_definition")
        items_for_cards = vocabulary_db.get_rnd_items(num_cards)
        card_items = []
        for i4c in items_for_cards:
            card = {"front_subtext": "", "back_subtext": ""}
            if mode == "ru2en":
                card["front_text"] = i4c.ru_translate
                if is_definition is not None:
                    card["front_subtext"] = i4c.definition
                card["back_text"] = i4c.word
                if is_example is not None:
                    card["back_subtext"] = i4c.example
            elif mode == "en2ru":
                card["front_text"] = i4c.word
                if is_definition is not None:
                    card["front_subtext"] = i4c.example
                card["back_text"] = i4c.ru_translate
                if is_example is not None:
                    card["back_subtext"] = i4c.definition
            else:
                raise ValueError('Unsupported cards mode')
            card_items.append(card)
        cards_db.set_cards(card_items)
        current_card = 1
    elif request.method == "GET":
        cache.clear()
        current_card = request.GET.get("current_card")
        if current_card is None:
            return create_cards(request)
        num_cards = cards_db.get_number()
    else:
        return create_cards(request)
    current_card = (int(current_card) - 1) % num_cards + 1
    cur_item = cards_db.get(current_card)
    prev_card = current_card - 1 if current_card > 1 else None
    next_card = current_card + 1 if current_card < num_cards else None
    context = {"num_cards": num_cards,
               "prev_card": prev_card,
               "current_card": current_card,
               "next_card": next_card,
               "front_text": cur_item.front_text,
               "front_subtext": cur_item.front_subtext,
               "back_text": cur_item.back_text,
               "back_subtext": cur_item.back_subtext,
               }
    return render(request, "cards.html", context)
