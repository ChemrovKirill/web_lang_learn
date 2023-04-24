from web_lang_learn.models import Cards

def set_cards(items):
    Cards.objects.all().delete()
    for i, item in enumerate(items):
        card_item = Cards(word=item["word"], 
                         ru_translate=item["ru_translate"], 
                         definition=item["definition"], 
                         number=i+1
                         )
        card_item.save()

def get(n):
    return Cards.objects.get(number=n)

def get_number():
    return Cards.objects.all().count()