# Don't really think this is a solution, although the graph is promising
# TODO How would I look at specifically the last second, or last 2 seconds of information
# How much data will need to be called or analyzed, how long does information need to be held in the program
# YFinance library https://pypi.org/project/yfinance/

# Raw Package
import numpy as np
import pandas as pd

#Data Source
import yfinance as yf

#Data viz
import plotly.graph_objs as go



class trading():
    def __init__(self, ticker, period = '1d', interval = '1m'):
        self.ticker = ticker
        self.period = period
        self.interval = interval
        self.data = yf.download(tickers=self.ticker, period = self.period, interval = self.interval)

    def sell(self): # Method to purchase a stock
        pass

    def buy(self): # Method to sell a stock
        pass

    def createGraph(self):
        # Interval required 1 minute
        data = yf.download(tickers=self.ticker, period=self.period, interval=self.interval)

        # declare figure
        fig = go.Figure()

        # Candlestick
        fig.add_trace(go.Candlestick(x=data.index,
                                     open=data['Open'],
                                     high=data['High'],
                                     low=data['Low'],
                                     close=data['Close'], name='market data'))

        # Add titles
        fig.update_layout(
            title='Apple live share price evolution',
            yaxis_title='Stock Price (USD per Shares)')

        # X-Axes
        fig.update_xaxes(
            rangeslider_visible=True,
            rangeselector=dict(
                buttons=list([
                    dict(count=15, label="15m", step="minute", stepmode="backward"),
                    dict(count=45, label="45m", step="minute", stepmode="backward"),
                    dict(count=1, label="HTD", step="hour", stepmode="todate"),
                    dict(count=3, label="3h", step="hour", stepmode="backward"),
                    dict(step="all")
                ])
            )
        )

        # Show
        fig.show()