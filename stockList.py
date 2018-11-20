# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 11:24:09 2018

@author: Wes Nicol
"""


from yahoo_fin import stock_info as si # documentation: http://theautomatic.net/yahoo_fin-documentation/

dow_tickers = si.tickers_dow()
#nasdaq_tickers = si.tickers_nasdaq()

def makeCurrency(num):
    return '${:,.2f}'.format(num)

def getDOWStocksUnder(price_threshold):
    print('DOW stocks under', makeCurrency(price_threshold), ':')


    for ticker in dow_tickers:
        #print(ticker, '\t', '${:,.2f}'.format(si.get_live_price(ticker)))

        if(si.get_live_price(ticker) < price_threshold):
            print(ticker, '\t',makeCurrency(si.get_live_price(ticker)))
            
    print('Done with DOW!')
    print()
    print()
            
def getNASDAQStocksUnder(price_threshold):
    print('NASDAQ stocks under', makeCurrency(price_threshold), ':')


    for ticker in nasdaq_tickers:
        #print(ticker, '\t', '${:,.2f}'.format(si.get_live_price(ticker)))

        if(si.get_live_price(ticker) < price_threshold):
            print(ticker, '\t',makeCurrency(si.get_live_price(ticker)))

    print('Done with NASDAQ!')
    print()
    print()



price_threshold = float(input('Enter the price threshold:\t$'))
getDOWStocksUnder(price_threshold)
getNASDAQStocksUnder(price_threshold)

