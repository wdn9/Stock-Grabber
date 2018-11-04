# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 10:31:14 2018

@author: Wes Nicol
"""

# import libraries
import urllib.request
from bs4 import BeautifulSoup


#URL of the webpage being scraped
url = 'https://finance.yahoo.com/quote/%5EDJI/'

# query the website and return the html to the variable ‘page’
page = urllib.request.urlopen(url)


# parse the html using beautiful soup and store in variable `soup`
soup = BeautifulSoup(page, 'html.parser')

'''
print(soup.prettify())
print()
print()
'''

#grab the actual current market index
marketIndexTag = soup.find('span',
                           class_="Trsdu(0.3s) Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(b)")


# grab the amount of change in the current day
dayChangeTag = soup.find('span',
                         class_="Trsdu(0.3s) Fw(500) Fz(14px) C($dataRed)")


print(marketIndex.text)
print()

print(dayChange.text)
print()























