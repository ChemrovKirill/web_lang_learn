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