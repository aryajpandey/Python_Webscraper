from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import html5lib

# this is a webscraper

driver = webdriver.Chrome('chromedriver_win32/chromedriver.exe')

quote = []
author = []
driver.get('https://www.goodreads.com/quotes')

content = driver.page_source
soup = BeautifulSoup(content, 'html5lib')

for a in soup.findAll('div', attrs={'class': 'quote'}):
    quotes = a.find('div', attrs={'class': 'quoteText'})
    authors = a.find('span', attrs={'class': 'authorOrTitle'})
    quote.append(quotes.text)
    author.append(authors.text)

popular_quotes = {'quote': quote, 'author': author}

inspire = pd.DataFrame(popular_quotes)

inspire.to_csv('quotes.csv', index=False, encoding='utf-8')
