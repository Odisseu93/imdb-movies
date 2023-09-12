import requests
from bs4 import BeautifulSoup

url = 'https://www.imdb.com/chart/top'

headers = {'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
(KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"}


site = requests.get(url, headers= headers)

soup = BeautifulSoup(site.content, 'html.parser')


lis = soup.findAll('li',{'class': 'ipc-metadata-list-summary-item'})
titles = soup.findAll('h3', {'class': 'ipc-title__text'})


for li in lis:
    print(li.text)

