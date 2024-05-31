import streamlit as st
from datetime import datetime
import time

current_datetime = datetime.now()
target_datetime = datetime(2023, 6, 2)
delta = current_datetime - target_datetime
days = delta.days

st.title("NarCountDown")
st.divider()
col1, col2, col3 = st.columns(3)
col1.subheader("Days Together:")
col3.subheader(days)
st.divider()
st.header("Progress Bars")
if days < 30:
    month_bar = st.progress(days / 30, text = "1 Month Together")
else:
    month_bar = st.progress(1.0, text = "1 Month Together")
if days < 183:
    sixmonth_bar = st.progress(days / 183, text = "6 Months Together")
else:
    sixmonth_bar = st.progress(1.0, text = "6 Months Together")
if days < 365:
    year_bar =  st.progress(days / 365, text = "1 Year Together")
else:
    year_bar = st.progress(1.0, text = "1 Year Together")
