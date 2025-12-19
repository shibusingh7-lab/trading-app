import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Binomo Predictor", layout="wide")
st.title("🚀 Ultimate Binomo Prediction App")
st.markdown("**RSI + MACD + Momentum + MA Combo | Timeframe ke Hisaab se Expiry Suggestion**")
st.warning("⚠️ Sirf demo/education ke liye! Real mein paise loss ho sakte hain. Demo account pe practice karo!")

# User input
col1, col2 = st.columns(2)
with col1:
    ticker = st.selectbox("Asset Choose Karo", 
                          ["EURUSD=X", "GBPUSD=X", "USDJPY=X", "AUDUSD=X", "USDCAD=X", "CRPTO/IDX=X",
                           "NZDUSD=X", "EURGBP=X", "BTC-USD", "ETH-USD", 
                           "AAPL", "GOOGL", "TSLA", "AMZN"])
with col2:
    timeframe = st.selectbox("Timeframe", 
                             ["1m", "2m", "5m", "15m", "30m", "60m"], 
                             index=2)

# Smart period options
if timeframe in ["1m", "2m"]:
    period_opts = ["1d", "2d", "5d", "7d"]
    default_p = "1d"
elif timeframe == "5m":
    period_opts = ["5d", "10d", "20d", "30d", "60d"]
    default_p = "5d"
else:
    period_opts = ["10d", "20d", "30d", "60d"]
    default
