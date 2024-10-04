from bs4 import BeautifulSoup
from urllib.parse import urljoin
import requests
from urllib.parse import urlparse

url = 'https://tululu.org/b5/'
response = requests.get(url)
response.raise_for_status()

soup = BeautifulSoup(response.text, 'lxml')
payload = 1

def download_image(url, payload, soup):
    url_art = urljoin(url, soup.find(class_='bookimage').find("img")['src'])
    response = requests.get(url_art, params=payload)
    response.raise_for_status() 
    image_url = urljoin(url, soup.find(class_='bookimage').find("img")['src'])
    filename = urlparse(image_url).path.split("/")[-1]
    print(url_art)
download_image(url, payload, soup)