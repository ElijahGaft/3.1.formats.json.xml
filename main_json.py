import json
from pprint import pprint
from collections import Counter

with open('newsafr.json', encoding='utf-8') as newsafr_file:
    news = (json.load(newsafr_file)).values()
    counter = 0
    text = []
    all_words = []
    for rss in news: # Проходимся по ключам в rss
        # pprint(rss)
        for kee_rss in rss.values():
            if type(kee_rss) == dict:
                # pprint(kee_rss.values())
                for items in kee_rss.values():
                    if type(items) == list:
                        # pprint(items)
                        for dict in items:
                            # pprint(dict.values())
                            for key_items in dict.values(): # Заходим в значения items по ключам
                                # pprint(key_items)
                                if counter == 3:
                                    text.append(key_items.split())
                                    counter += 1
                                elif counter == 5:
                                    counter = 0
                                else:
                                    counter += 1
                        for list_news in text:
                            for word in list_news:
                                if len(word) >= 6:
                                    all_words.append(word.lower())
    text_counts = Counter(all_words)
    top_ten = text_counts.most_common(10)
    pprint(top_ten)