# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 10:31:14 2018

@author: Wes Nicol
also Caleb Kress did stuff
"""

# import libraries
import requests
from BeautifulSoup import BeautifulSoup


#URL of the webpage being scraped
url = 'https://finance.yahoo.com/quote/%5EDJI/'

# query the website and return the html to the variable ‘page’
response = requests.get(url)
html = response.content

# parse the html using beautiful soup and store in variable `soup`
soup = BeautifulSoup(html)

#grab the actual current market index
marketIndexTag = soup.find('span', {'class': 'Trsdu(0.3s) Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(b)'}).text.replace(',', '')
print(marketIndexTag)

# grab the amount of change in the current day
if soup.find('span', {'class': 'Trsdu(0.3s) Fw(500) Fz(14px) C($dataRed)'}) == None:
    dayChangeTag = soup.find('span', {'class': 'Trsdu(0.3s) Fw(500) Fz(14px) C($dataGreen)'}).text.encode('utf-8').replace('(', '').replace(')', '').replace('+', '').replace('%', '')
else:
    dayChangeTag = soup.find('span', {'class': 'Trsdu(0.3s) Fw(500) Fz(14px) C($dataRed)'}).text.encode('utf-8').replace('(', '').replace(')', '').replace('+', '').replace('%', '')

#split day change from day change percentage
dayChangeList = dayChangeTag.split(' ')
print(dayChangeList)
