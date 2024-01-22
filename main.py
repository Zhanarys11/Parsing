import requests, json, csv, os, time
from dotenv import load_dotenv
from bs4 import BeautifulSoup

def get_html(url, header):
    response = requests.get(url, headers=header)

    if response.status_code == 200:
        return response.text
    else:
        raise Exception(f"Произощла ошибка при получении html: {response.status_code}")
    

def processing(html, id, domain):
    soup = BeautifulSoup(html, "lxml").find("div", {"class": "a-list"})
    soup = soup.find_all("div", {"class": "a-card"})

    info = []

    for a_card in soup:
        a_card__info = a_card.find("div", {"class": "a-card__info"})

        title = a_card__info.find("a", {"class": "a-card__link"}).get_text(strip=True)
        url = domain + a_card__info.find("a", {"class": "a-card__link"}).get("href")
        price = a_card__info.find("span", {"class": "a-card__price"}).get_text(strip=True)

        info_body = a_card__info.find("p", {"class": "a-card__description"}).get_text(strip=True).split(", ")
        info_footer = a_card.find("div", {"class": "a-card__data"})

        try: year = info_body[0]
        except: year = "Нет данных"

        try: condition = info_body[1]
        except: condition = "Нет данных"

        try:volume = info_body[2]
        except: volume = "Нет данных"

        try: fuel = info_body[3]
        except: fuel = "Нет данных"

        try: transmission = info_body[4]
        except: transmission = "Нет данных"
        
        try:
            mileage = info_body[5] if str(info_body[5]).endswith("км") else "Нет данных"
        except: 
            mileage = "Нет данных"
        
        try: color = info_body[6]
        except: color = "Нет данных"

        try: city = info_footer.find("span", {"class": "a-card__param"}).get_text(strip=True)
        except: city = "Нет данных"

        try: date = info_footer.find("span", {"class": "a-card__param--date"}).get_text(strip=True)
        except: date = "Нет данных"


        info.append({
            "id": id,
            "title": title,
            "url": url,
            "year": year,
            "condition": condition,
            "volume": volume,
            "fuel": fuel,
            "transmission": transmission,
            "mileage": mileage,
            "color": color,
            "price": price,
            "city": city,
            "date": date,
        })
        id += 1
    return info, id



def run_parser():
    load_dotenv()
    header = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0"}
    URL = os.getenv('URL')
    DOMAIN = os.getenv('DOMAIN')

    # html = get_html(URL, header)
    # data = processing(html, DOMAIN)

    big_data = []
    ID = 1
    for page in range(11, 14):
        if page > 1:
            URL = URL + f"?page={page}"

        html = get_html(URL, header)
        time.sleep(1)
        data, id = processing(html, ID, DOMAIN)
        ID = id
        big_data.extend(data)

        print(f"Обработана {page} страница")

    with open("data.json", "w") as file1:
        json.dump(big_data, file1, indent=4, ensure_ascii=False)

    with open("data.csv", "w") as file:
        writer = csv.writer(file)
        writer.writerow(
            (
                "id", "title", "url", "year", "condition", "volume", 
                "fuel", "transmission", "mileage", 
                "color", "price", "city", "date"
            )
        )
        for item in big_data:
            writer.writerow(
                (
                    item["id"], item["title"], 
                    item["url"], item["year"],
                    item["condition"], item["volume"], item["fuel"],
                    item["transmission"], item["mileage"], 
                    item["color"], item["price"],
                    item["city"], item["date"]
                )
            )

run_parser()
