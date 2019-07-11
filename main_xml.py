from collections import Counter
import xml.etree.ElementTree as ET
tree = ET.parse('newsafr.xml')
text = []
all_words = []
items = tree.findall('channel/item')
for item in items:
    news = item.find('description').text
    text.append(news.split())
# print(text)
for list_news in text:
    # print(list_news)
    for word in list_news:
        if len(word) >= 6:
            all_words.append(word)
# print(all_words)
text_counts = Counter(all_words)
top_ten = text_counts.most_common(10)
for answer in top_ten:
    print(answer)