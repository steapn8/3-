import requests
from pathlib import Path
from bs4 import BeautifulSoup

def check_for_redirect(response):
    if response.history :
       raise requests.HTTPError


def download_txt(url, payload):
    book_response = requests.get(url, params=payload)
    book_response.raise_for_status()
    check_for_redirect(book_response)
    with open(filepath, 'wb') as file:
        file.write(book_response.content)

Path("books").mkdir(parents=True, exist_ok=True)

for id in range(1,11):
    
    url = "https://tululu.org/txt.php"
    payload = {"id": id}
    try:
        
        
        page_url = f"https://tululu.org/b{id}"
        page_response = requests.get(page_url)
        page_response.raise_for_status()

        soup = BeautifulSoup(page_response.text, 'lxml')
        title_of_book = soup.find('h1')
        division_of_title  = title_of_book.text
        book_name = division_of_title.split('::')[0]
        book_name = book_name.replace(':', '')
        print(book_name)

        filepath = f'books/{book_name.strip(  )}.txt'
        
        download_txt(url, payload)
            

    except requests.HTTPError:
        print("такой книги нет ")

