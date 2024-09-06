from bs4 import BeautifulSoup
import requests

url = 'https://tululu.org/b1/'
response = requests.get(url)
response.raise_for_status()

soup = BeautifulSoup(response.text, 'lxml')
heading = soup.find('h1').text

print("Заголовок:", heading.split("::")[0], "\n", "Автор:", heading.split("::")[1].strip())


