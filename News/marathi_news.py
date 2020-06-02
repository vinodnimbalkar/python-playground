import requests
from bs4 import BeautifulSoup
import pandas as pd

#specify the url of marathi news website
url = "http://lokmat.com/"

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
news = soup.find('ul', class_='live-news-list')

for i in news.findAll('li'):
	data = i.text
	print(data)
