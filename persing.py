# └── Создания Парсера
#     ├── get_html()
#     ├── processing()
#     └── run_parser()

import requests, json, csv
from bs4 import BeautifulSoup

def get_html(url, header):
    """
        get_html(url, header)

        url: Адрес сайта которую вы хотите спарсить
        header: Заголовок в сети

        Возвращает html страницу которую мы хотим спарсить
        Если не сможет получить html возвращает ошибку 
        Если все хорошо возвращает html страницу которую мы хотим спрасить

        Используется для получения html страницы которую мы хотим спарсить

    """

    responce = requests.get(url, headers=header)

    if responce.status_code == 200:
        return responce.text
    
    else:
        raise Exception(f"Произошла ошибка при получении страницы: {responce.status_code}")
    

def processing(html, id, page):
    """
        processing(html)


        html: html страница которую мы хотим спарсить

        Возвращает данные которые мы хотим отобразить в таблице
        Если не сможет получить данные возвращает ошибку
        Если все хорошо возвращает данные которые мы хотим отобразить в таблице

        Используется для обработки html страницы которую мы хотим спарсить
    """

    soup = BeautifulSoup(html, "lxml").find("div", {"id": "dle-content"})

    soup = soup.find_all("div", {"class": "shortstory"})

    info = []
    
    for shortstory in soup:
        temp_a = shortstory.find("div", {"class":"shortstoryHead"}).find("a")
        temp_p = shortstory.find("div", {"class":"shortstoryContent"}).find_all("p")
        temp_main_content = shortstory.find("div", {"class": "shortstoryContent"})
        temp_div = temp_main_content.find_all("div")

        image_url = "https://v2.vost.pw/" + temp_div[0].find("img").get("src")
        try:
            rating = temp_div[1].find("li", {"class": "current-rating"}).text + "%"
            vote = temp_div[1].find("span").find("span").text + " голосов"
        except:
            vote = None
            rating = None

        title = temp_a.text.split(" /")[0]
        url = temp_a.get("href")
        year = (f"{temp_p[0].text.split(': ')[1].title()}г")
        genre = temp_p[1].text.split(": ")[1].title()
        types = temp_p[2].text.split(": ")[1]
        episodes = temp_p[3].text.split(": ")[1]

        if len(temp_p[4].text.split()) <= 5:
            director = temp_p[4].text.split(": ")[1]
        else:
            director = None  


        info.append({
            "id": id,
            "title": title,
            "url": url,
            "year": year,
            "genre": genre,
            "types": types,
            "episodes": episodes,
            "director": director,
            "vote": vote,
            "rating": rating,
            "image_url": image_url,
            "page": page
        })
        id += 1

    return info, id


def run_parser():
    url = "https://v2.vost.pw/"
    header = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:121.0) Gecko/20100101 Firefox/121.0"}

    big_date = []
    ID = 1
    for page in range(1,310):

        html = get_html(url + f"/page/{page}/", header)
        data, id = processing(html, ID, page)
        ID = id
        big_date.extend(data)
        print(f"Обработана {page} страниц")

    with open("v2.vost.json", "w") as file:
        json.dump(big_date, file, indent=4, ensure_ascii=False)

    return "Парсинг окончен"

print(run_parser())