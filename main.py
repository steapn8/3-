import requests
from pathlib import Path
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from urllib.parse import urlparse


def check_for_redirect(response):
    if response.history :
       raise requests.HTTPError


def download_txt(filepath, response):
    
    with open(filepath, 'wb') as file:
        file.write(response.content)
    

def download_image(url, payload):
    url_art = urljoin(url, soup.find(class_='bookimage').find("img")['src'])
    response = requests.get(url_art, params=payload)
    response.raise_for_status() 
    image_url = urljoin(url, soup.find(class_='bookimage').find("img")['src'])
    filename = urlparse(image_url).path.split("/")[-1]

    filepath = f'image/{filename}'
    with open(filepath, 'wb') as file:
        file.write(response.content)

Path("books").mkdir(parents=True, exist_ok=True)
Path("image").mkdir(parents=True, exist_ok=True)

for id in range(1,11):
    
    url = "https://tululu.org/txt.php"
    payload = {"id": id}
    try:
        
        book_response = requests.get(url, params=payload)
        book_response.raise_for_status()
        check_for_redirect(book_response)
        page_url = f"https://tululu.org/b{id}"
        
        page_response = requests.get(page_url)
        page_response.raise_for_status()

        soup = BeautifulSoup(page_response.text, 'lxml')
        title_of_book = soup.find('h1')
        division_of_title  = title_of_book.text
        book_name = division_of_title.split('::')[0]
        book_name = book_name.replace(':', '')
        print("\n", book_name)
        list_comments = soup.find_all(class_='texts')
        #print(list_comments)
        for comment in list_comments:
            print(comment.find(class_='black').text)

        filepath = f'books/{book_name.strip(  )}.txt'
        
        download_txt(filepath, book_response)
        download_image(url, payload)


    except requests.HTTPError:
        print("такой книги нет ")

