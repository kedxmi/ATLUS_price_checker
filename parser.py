import requests
from bs4 import BeautifulSoup

URL = "https://steamdb.info/developer/ATLUS/"

headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(URL, params={"displayOnly": "Game"}, headers=headers)

soup = BeautifulSoup(response.text, "lxml")
games = soup.find_all('tr', class_='app')

for game in games:
    title = game.find(class_='b')
    price = game.find_all('td')[4]

    title = title.text.strip()
    price = price.text.strip()

    print(title)
    print(price)
