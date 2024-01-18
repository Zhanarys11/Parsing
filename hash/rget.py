# HTTP - Hypertext Transfer Protocol
# HTTPS - Hypertext Transfer Protocol Secure
# TCP - Transmission Control Protocol
# UDP - User Datagram Protocol

# POST, GET, PUT, DELETE
# CRUD - Create, Read, Update, Delete

# REQUEST - запрос клиента
# STATUS CODE - код ответа
# RESPONCE - ответ сервера

# responce виды ответов: content, text, json
from bs4 import BeautifulSoup

import requests
import json

with open("index.html", "r") as file:
    html = file.read()

#html.parser, lxml

soup = BeautifulSoup(html, "lxml").find("div", {"id": "dle-content"}).find_all("div", {"class": "shortstory"})

info = []

for shortstory in soup:
    d = shortstory.find("div", {"class":"shortstoryHead"}).find("a")
    title = d.text.split("/")[0]
    url = d.get("href")

    year = shortstory.find("div", {"class":"shortstoryContent"}).find_all("p")[0].text

    zhanr = shortstory.find("div", {"class":"shortstoryContent"}).find_all("p")[1].text

    info.append({
        "title": title,
        "url": url,
        "year": year,
        "zhanr": zhanr
    })


with open("info.json", "w") as file:
    json.dump(info, file, indent = 4, ensure_ascii=False)


# url = "https://v2.vost.pw/"

# response = requests.get(url)

# if response.status_code == 200:
#     #print(response.text)
#     with open("index.html", "w") as file:
#         file.write(response.text)

# else:
#     print("Error", response.status_code)