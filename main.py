import requests
from pathlib import Path


Path("books").mkdir(parents=True, exist_ok=True)


for id in range(1,11):
    filepath = f'books/book_{id}.txt'
    url = "https://tululu.org/txt.php"
    payload = {"id": id}

    response = requests.get(url, params=payload)
    response.raise_for_status()
  
  
    with open(filepath, 'wb') as file:
        file.write(response.content)