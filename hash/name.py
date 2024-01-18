import requests
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

responce = requests.get("https://rickandmortyapi.com/api/location/1")
if responce.status_code == 200:
    print(responce.json())
    # with open("IMAGE.jpg", "wb") as file:
    #     file.write(responce.content)