from web_lang_learn.models import Vocabulary

def get_items_for_table():
    items = []
    for i, item in enumerate(Vocabulary.objects.all()):
        items.append([i+1, 
                      item.word, 
                      item.ru_translate, 
                      item.definition, 
                      item.example if item.example else '', 
                      item.comment if item.comment else '',
                      ])
    return items

def add_word(item):
    voc_item = Vocabulary(word=item["word"], 
                          ru_translate=item["ru_translate"], 
                          definition=item["definition"], 
                          example=item["example"],
                          comment=item["comment"]
                         )
    voc_item.save()

def in_db(word):
    if Vocabulary.objects.filter(word=word) is None:
        return False
    else:
        return True