import streamlit as st
import time

st.title("NarStudy")

st.markdown("Use this as a timer to study!")

def count_down(ts):
    with st.empty():
        while ts:
            mins, secs = divmod(ts, 60)
            time_now = '{:02d}:{:02d}'.format(mins, secs)
            st.header(f"{time_now}")
            time.sleep(1)
            ts -= 1
        st.header("Times Up! Good work babe!")

time_in_seconds = 30 * 60

if st.button("START"):
        count_down(int(time_in_seconds))



