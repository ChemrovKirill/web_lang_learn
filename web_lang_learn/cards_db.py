from web_lang_learn.models import Cards

def set_cards(items):
    Cards.objects.all().delete()
    for i, item in enumerate(items):
        card_item = Cards(front_text=item["front_text"],
                          back_text=item["back_text"],
                          front_subtext=item["front_subtext"],
                          back_subtext=item["back_subtext"],
                          number=i+1
                          )
        card_item.save()

def get(n):
    return Cards.objects.get(number=n)

def get_number():
    return Cards.objects.all().count()