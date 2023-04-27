"""
Module for working with database of cards
"""

from web_lang_learn.models import Cards

def set_cards(items):
    """ replaces old cards in database with new set of cards """
    Cards.objects.all().delete()
    for i, item in enumerate(items):
        card_item = Cards(front_text=item["front_text"],
                          back_text=item["back_text"],
                          front_subtext=item["front_subtext"],
                          back_subtext=item["back_subtext"],
                          number=i+1
                          )
        card_item.save()

def get(number):
    """ returns card with given number """
    return Cards.objects.get(number=number)

def get_number():
    """ returns number of cards in database """
    return Cards.objects.all().count()
