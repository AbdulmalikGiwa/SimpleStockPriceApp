import yfinance as yf
import streamlit as st
import json

st.write("""
# TESLA Stock price App
""")

tickerSymbol = 'TSLA'
tickerData = yf.Ticker(tickerSymbol)

pyject = tickerData.info

st.write(pyject['longBusinessSummary'])

tickerDf = tickerData.history(period='1d', start='2019-11-20', end='2020-06-10')

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)

