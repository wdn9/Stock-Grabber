# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 10:31:14 2018

@author: Wes Nicol
"""

# import libraries
import urllib.request
from bs4 import BeautifulSoup


# this function reutrns the current index of the DOW Jones (according to cnn) as a float
def getDOWIndex():
    url = 'https://money.cnn.com/data/markets/dow/'

    # query the website and return the html to the variable ‘page’
    page = urllib.request.urlopen(url)
    
    # parse the html using beautiful soup and store in variable `soup`
    soup = BeautifulSoup(page, 'html.parser')

    marketIndexTag = soup.find('span',stream='last_599362')
    
    #grab the actual current market index
    currentIndex = marketIndexTag.text
    
    
    #remove comma from current index number
    currentIndex = currentIndex.replace(',', '')
    
    #convert currentIndex to float
    currentIndex = float(currentIndex)
    
    
    return currentIndex




def getDayChange():
    url = 'https://money.cnn.com/data/markets/dow/'

    # query the website and return the html to the variable ‘page’
    page = urllib.request.urlopen(url)

    # parse the html using beautiful soup and store in variable `soup`
    soup = BeautifulSoup(page, 'html.parser')
    
    # grab the amount of change in the current day
    dayChangeTag = soup.find('span',class_='posData')
    #if positive change isnt found, look for negitive one
    if(dayChangeTag is None): 
        dayChangeTag = soup.find('span',class_='negData')
    
    dayChangeText = dayChangeTag.text
    
    return float(dayChangeText)

    
def getDayChangePercentage():
    url = 'https://money.cnn.com/data/markets/dow/'

    # query the website and return the html to the variable ‘page’
    page = urllib.request.urlopen(url)
    
    # parse the html using beautiful soup and store in variable `soup`
    soup = BeautifulSoup(page, 'html.parser')

    # grab the amount of change in the current day
    dayChangeTag = soup.find_all('span',class_='posData')
    
    # index 1 is used because thats where the data is stored in the html document
    dayChangeText = dayChangeTag[1].text


    #strip '(',')' & '%' from percentage
    dayChangeText = dayChangeText.replace(')', '')
    dayChangeText = dayChangeText.replace('(', '')
    dayChangeText = dayChangeText.replace('%', '')

    return float(dayChangeText)

'''
print('DOWIndex:\t\t' + str(getDOWIndex()))
print('Current Day Channge:\t' + str(getDayChange()))
print('Precentage Change:\t' + str(getDayChangePercentage()) + '%')
'''













