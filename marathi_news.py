#!/usr/bin/python (No need to write Python before file)
import urllib.request
from bs4 import BeautifulSoup
import pandas as pd

#specify the url of marathi news website
url = "http://www.lokmat.com/"

page = urllib.request.urlopen(url)
soup = BeautifulSoup(page, 'html.parser')
news = soup.find('ul', class_='vertical-ticker')


for i in news.findAll('li'):
	cells = i.find('a')
	data = cells.text
	print(data)