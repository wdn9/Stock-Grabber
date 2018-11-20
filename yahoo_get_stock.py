# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 10:07:14 2018

@author: Wes Nicol

This file is very much like the getIndex file, but supposedly a library has already been
written to do what I was trying to do with the getIndex.py file. Lets see if they did it better (probably)


If you want to use a more in depth stock API follow this URL (it cost money though!)
https://intrinio.com/

"""

from yahoo_fin import stock_info as si
from time import sleep


ticker = 'AMZN'
current_time = 0
# infinite loop shows how quickly this information can update
while(True):
    print(current_time)
    print(ticker, ' current price: ', si.get_live_price(ticker))
    print()
    
    current_time += 5
    sleep(5)


