from bs4 import BeautifulSoup
import urllib.request
import re
import time
import random
import src.mongo_handler as mongo
import src.producer as producer

def links_from_soup(soup):
    links = []
    for a in soup.find_all('a'):
        link = re.findall(r"<a href=\"\/wiki\/(.+)\" title=\".+\">",
                          str(a),
                          re.DOTALL)
        if link:
            if ':' not in str(link[0]):
                links.append(link[0])
    return links


def text_from_soup(soup):
    text = ''
    for p in soup.select('p'):
        text = re.sub(r"[^a-z|ąćęłóśńżź|\s]", ' ',
                      p.get_text().lower())  # usuwanie liczb, nawiasów, znaków interpunkcyjnych zamiana na małe litery
        text = re.sub(' +', ' ', text)  # usuwanie podwójnych spacji

    return text


scraped_links = set(mongo.get_scraped_links())
links_to_scrap = set(mongo.get_links_to_scrap())

print(len(links_to_scrap) - len(scraped_links))
# print(len(scraped_links))

i = 0
for l in links_to_scrap:
    if l in scraped_links:
        continue
    try:
        fp = urllib.request.urlopen("https://pl.wikipedia.org/wiki/" + str(l))
        page = fp.read().decode("utf8")
        fp.close()
    except:
        continue

    soup = BeautifulSoup(page, 'html.parser')
    new_links = links_from_soup(soup)
    try:
        text = text_from_soup(soup)
        producer.produce(l, text)
    except:
        continue









print(i)