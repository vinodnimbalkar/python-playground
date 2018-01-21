#!/usr/bin/python (No need to write Python before file)
import urllib.request
from bs4 import BeautifulSoup
import pandas as pd

#specify the url of marathi news website
url = "http://www.lokmat.com/"

page = urllib.request.urlopen(url)
soup = BeautifulSoup(page, 'html.parser')
news = soup.find('ul', class_='live-news-list')

for i in news.findAll('li'):
	data = i.text
	print(data)
