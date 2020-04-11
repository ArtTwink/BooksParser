import urllib.request
import urllib.parse
import re
import json
from tabulate import tabulate
import requests
import random
from bs4 import BeautifulSoup

r = urllib.request.urlopen("https://libs.ru/best-100-russian/")
soup = BeautifulSoup(r, features="html.parser")

# Description
desc = []
for tag in soup.find_all("div", class_="book-cardLong-descr"):
    desc.append(tag.text.strip(" Читать онлайн").strip('\n\r\t').replace(u'\xa0', u' '))
# print(desc)

# Name
soup_name = []
for tag in soup.find_all("div", class_="book-cardLong-name"):
    soup_name.append(tag.text.replace(u'\xa0', u' '))
name = [re.sub(r'#(\d+ )', '', i) for i in soup_name]
# print(name)

# Author
author = []
for tag in soup.find_all("a", class_="book-cardLong-author"):
    if tag.text == "Евгений Петров":
        author.append("Евгений Петров, Ильф Илья")
    elif tag.text == "Ильф Илья":
        continue
    elif tag.text == 'Федор Михайлович Достоевский':
        continue
    elif tag.text == "Галина Юдина":
        continue
    else:
        author.append(tag.text)
# print(author)

# print(len(desc), len(name), len(author))
rand = random.randrange(len(name))
# print(author[rand], name[rand], desc[rand], sep='\n')

API_ENDPOINT = "http://localhost:8080/books"
data = {
    "title": name[rand],
    "description": desc[rand],
    "author": author[rand]
}
# print(data)
r = requests.post(url=API_ENDPOINT, data=json.dumps(data))
print(r.text, r.status_code)