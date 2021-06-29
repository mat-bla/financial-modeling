#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 00:03:04 2021

@author: Matthew Blair
"""

import mplfinance as mpf 
import datetime as dt
import pandas_datareader as pdr 
import matplotlib.pyplot as plt


now = dt.datetime.now()
start = now - dt.timedelta(90)
ticker = "SPY"
style = 'yahoo'
chartType = 'candle'
filename = ticker.lower()+'.png'
df = pdr.get_data_yahoo(ticker ,start , now)

mpf.plot(df,
         type=chartType,
         style=style,
         volume=True,
         mav=(10,20,50),
         title=ticker+str("\n$"+str(df['Close'][-1])[0:7])
         )

plt.savefig(filename,dpi=400)
