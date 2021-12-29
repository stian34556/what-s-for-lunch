# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'}
url = 'https://www.yelp.ca/search?cflt=restaurants&find_loc=Vancouver%2C+BC'
response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.content, 'lxml')

for item in soup.select('[class*=container]'):
    try:
        # print(item)
        if item.find('h4'):
            name = item.find('h4').get_text()
            print(name)
            print(soup.select('[class*=reviewCount]')[0].get_text())
            #print(soup.select('[class*=reviewCount]')[0].get_text())
            #print(soup.select('[aria-label*=rating]')[0]['aria-label'])
            #print(soup.select('[class*=secondaryAttributes]')[0].get_text())
            #print(soup.select('[class*=priceRange]')[0].get_text())
            #print(soup.select('[class*=priceCategory]')[0].get_text())
            print('------------------')
    except Exception as e:
        raise e
        print('')
