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

    soup = BeautifulSoup(page_response.text, 'lxml')
    image_url = soup.find(class_='bookimage').find("img")['src']
    title_of_book = soup.find('h1')
    division_of_title  = title_of_book.text
    book_name = division_of_title.split('::')[0]
    book_name = book_name.replace(':', '')
    author = division_of_title.split('::')[1]
    author = author.replace(':', '')

    list_comments = soup.find_all(class_='texts')
    comments = []
    for comment in list_comments:
        comments.append(comment.find(class_='black').text)

    genres = []
    list_genre = soup.find(id = "content").find_all(class_ = "d_book")
    genres_links = list_genre[1].find_all("a")
    for genres_link in genres_links:
        genres.append(genres_link.text)
    book_parameters = {
        'image_url':image_url,
        'book_name':book_name,
        'author':author,
        'comments':comments,
        'genres':genres,
    }
    return book_parameters 



def main():
    url = "https://tululu.org/txt.php"
    Path("books").mkdir(parents=True, exist_ok=True)
    Path("image").mkdir(parents=True, exist_ok=True)

    parser = argparse.ArgumentParser(
        description='программа скачивает книги и изображение с сайта https://tululu.org'
    )
    parser.add_argument ('--start_id', type=int, default=1, help="первая книга" )
    parser.add_argument ('--end_id', type=int, default=11, help="финальная книга")
    args = parser.parse_args()


    for book_id in range(args.start_id, args.end_id):
        payload = {"id": book_id}
        try:
            
            book_response = requests.get(url, params=payload)
            book_response.raise_for_status()
            check_for_redirect(book_response)
            page_url = f"https://tululu.org/b{book_id}/"
            page_response = requests.get(page_url)
            page_response.raise_for_status()
            check_for_redirect(page_response)

            book_parameters = parse_book_page(page_response)



            filepath = f'books/{book_parameters['book_name'].strip(  )}.txt'
            
            download_txt(filepath, book_response)
            download_image(payload, page_url + book_parameters['image_url'])


        except requests.HTTPError:
            print("\n такой книги нет ")
        except requests.ConnectionError:
            print("\n Потеря с интернетом.")

if __name__ == '__main__':
    
    main()
    