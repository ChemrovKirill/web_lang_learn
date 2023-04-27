import random

from web_lang_learn.models import Vocabulary


def get_items_for_table():
    """
    return all the words from the vocabulary
    database to make a table
    """
    items = []
    for i, item in enumerate(Vocabulary.objects.all().order_by('-id')):
        items.append([i+1,
                      item.word,
                      item.ru_translate,
                      item.definition,
                      item.example if item.example else '',
                      item.comment if item.comment else '',
                      ])
    return items


def add_word(item):
    """ adds a word to the vocabulary """
    voc_item = Vocabulary(word=item["word"].lower(),
                          ru_translate=item["ru_translate"],
                          definition=item["definition"],
                          example=item["example"],
                          comment=item["comment"]
                          )
    voc_item.save()


def in_db(word):
    """ check if the word is already in the vocabulary database """
    if Vocabulary.objects.filter(word=word.lower()).count() == 0:
        return False
    return True


def get_rnd_items(k):
    """
    returns k random items from the vocabulary
    (with repetitions if k > number of words in the vocabulary)
    """
    voc_items = Vocabulary.objects.all()
    if k <= voc_items.count():
        return random.sample(list(voc_items), k=k)
    return random.choices(list(voc_items), k=k)
