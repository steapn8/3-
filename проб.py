from bs4 import BeautifulSoup
from urllib.parse import urljoin
import requests
from urllib.parse import urlparse

import sys
import argparse
url = 'https://tululu.org/b5/'
response = requests.get(url)
response.raise_for_status()

soup = BeautifulSoup(response.text, 'lxml')



#parser.add_argument ('count', type=int)
#for _ in range (namespace.count):
 
def createParser ():
    parser = argparse.ArgumentParser()
    parser.add_argument ('start_id', type=int)
    parser.add_argument ('end_id', type=int)
 
    return parser
 
 

parser = createParser()
namespace = parser.parse_args(sys.argv[1:])

print (namespace)

for _ in range (namespace.start_id, namespace.end_id + 1):
    print(_)