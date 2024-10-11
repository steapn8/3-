import requests
from pathlib import Path
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from urllib.parse import urlparse
import argparse


def check_for_redirect(response):
    if response.history :
       raise requests.HTTPError


def download_txt(filepath, response):
    
    with open(filepath, 'wb') as file:
        file.write(response.content)
    

def download_image(payload, image_url):
    
    response = requests.get(image_url, params=payload)
    response.raise_for_status() 
    filename = urlparse(image_url).path.split("/")[-1]

    filepath = f'image/{filename}'
    with open(filepath, 'wb') as file:
        file.write(response.content)



def parse_book_page(page_response):
    data_from_parsing = {}
    soup = BeautifulSoup(page_response.text, 'lxml')
    image_url = urljoin(url, soup.find(class_='bookimage').find("img")['src'])
    data_from_parsing['image_url'] = image_url
    title_of_book = soup.find('h1')
    division_of_title  = title_of_book.text
    book_name = division_of_title.split('::')[0]
    book_name = book_name.replace(':', '')
    print("\n", book_name)
    data_from_parsing['book_name'] = book_name
    author = division_of_title.split('::')[1]
    author = author.replace(':', '')
    print(author)
    data_from_parsing['author'] = author

    list_comments = soup.find_all(class_='texts')
    comments = []
    #print(list_comments)
    for comment in list_comments:
        comments.append(comment.find(class_='black').text)
    #print(comments)
    data_from_parsing['comments'] = comments

    genres = []
    list_genre = soup.find(id = "content").find_all(class_ = "d_book")
    genres_links = list_genre[1].find_all("a")
    for genres_link in genres_links:
        genres.append(genres_link.text)
    #print(genres)
    data_from_parsing['genres'] = genres
    return data_from_parsing 

Path("books").mkdir(parents=True, exist_ok=True)
Path("image").mkdir(parents=True, exist_ok=True)

parser = argparse.ArgumentParser(
    description='программа скачивает книги и изображение с сайта https://tululu.org'
)
parser.add_argument ('--start_id', type=int, default=1, help="первая книга" )
parser.add_argument ('--end_id', type=int, default=11, help="финальная книга")
args = parser.parse_args()


for id in range (args.start_id, args.end_id):
    
    url = "https://tululu.org/txt.php"
    payload = {"id": id}
    try:
        
        book_response = requests.get(url, params=payload)
        book_response.raise_for_status()
        check_for_redirect(book_response)
        page_url = f"https://tululu.org/b{id}"
        page_response = requests.get(page_url)
        page_response.raise_for_status()


        parse_book = parse_book_page(page_response)


        filepath = f'books/{parse_book['book_name'].strip(  )}.txt'
        
        download_txt(filepath, book_response)
        download_image(payload, parse_book['image_url'])


    except requests.HTTPError:
        print("\n такой книги нет ")

