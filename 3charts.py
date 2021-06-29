#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 13:20:59 2021

@author: matthew blair
"""

import mplfinance as mpf 
import datetime as dt
import pandas_datareader as pdr 
import matplotlib.pyplot as plt
import talib

#adjust start parameters to set the time period, in days
now = dt.datetime.now()
start = now - dt.timedelta(120)
stock = "SPY"
stock2 = "BTC-USD"
stock3 = "ETH-USD"
style = 'binance'
chartType = 'candle'
df = pdr.get_data_yahoo(stock ,start , now)
df2 = pdr.get_data_yahoo(stock2 ,start , now)
df3 = pdr.get_data_yahoo(stock3 ,start , now)

#Calculates the RSI for each chart
df["rsi"] = talib.RSI(df['Close'])
df2["rsi"] = talib.RSI(df2['Close'])
df3["rsi"] = talib.RSI(df3['Close'])



fig = mpf.figure(figsize=(16,10))

#These aren't in the right order, sorry if that's confusing
ax1 = fig.add_subplot(3,3,1)
ax2 = fig.add_subplot(3,3,2)
ax5 = fig.add_subplot(3,3,3)

av1 = fig.add_subplot(3,3,4)
av2 = fig.add_subplot(3,3,5)
av3 = fig.add_subplot(3,3,7)
av4 = fig.add_subplot(3,3,8)
av5 = fig.add_subplot(3,3,9)
av6 = fig.add_subplot(3,3,6)


apdict = mpf.make_addplot(df['rsi'],type='line',ax=av3)
apdict2 = mpf.make_addplot(df2['rsi'],type='line',ax=av4)
apdict3 = mpf.make_addplot(df3['rsi'],type='line',ax=av5)


#Uncomment this code if the markets tank and you need a seratonin boost :)

#df['Close'][-1]=float(df['Open'][-1]*1.8)
#df2['Close'][-1]=float(df2['Open'][-1]*1.8)
#df3['Close'][-1]=float(df3['Open'][-1]*1.8)


#adjust the mav numbers to change which moving averages are shown

mpf.plot(df,
         type=chartType,
         style=style,
         ax=ax1,
         volume=av1,
         addplot=apdict,
         mav=(10,20,50),
         axtitle=stock+str("\n$"+str(df['Close'][-1])[0:7])
         )


mpf.plot(df2,
         type=chartType,
         style=style,
         ax=ax2,
         volume=av2,
         addplot=apdict2,
         mav=(10,20,50),
         axtitle=stock2+str("\n$"+str(df2['Close'][-1])[0:7])
         )


mpf.plot(df3,
         type=chartType,
         style=style,
         ax=ax5,
         volume=av6,
         addplot=apdict3,
         mav=(10,20,50),
         axtitle=stock3+str("\n$"+str(df3['Close'][-1])[0:7])
         )


fig.tight_layout()
plt.savefig("3charts.png",dpi=400)







