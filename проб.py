from bs4 import BeautifulSoup
from urllib.parse import urljoin
import requests
from urllib.parse import urlparse

url = 'https://tululu.org/b5/'
response = requests.get(url)
response.raise_for_status()

soup = BeautifulSoup(response.text, 'lxml')

#print(soup.find_all(class_='texts'))
genres = []
list_genre = soup.find(id = "content").find_all(class_ = "d_book")
genres_links = list_genre[1].find_all("a")
for genres_link in genres_links:
    genres.append(genres_link.text)
print(genres)