from bs4 import BeautifulSoup
from urllib.parse import urljoin
import requests
from urllib.parse import urlparse

url = 'https://tululu.org/b9/'
response = requests.get(url)
response.raise_for_status()

soup = BeautifulSoup(response.text, 'lxml')

#print(soup.find_all(class_='texts'))
list_comments = soup.find_all(class_='texts')

for comment in list_comments:
    print(comment.find(class_='black').text)