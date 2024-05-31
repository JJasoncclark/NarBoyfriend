import streamlit as st

st.set_page_config(
    page_title="NarBoyfriend"
)
st.title("Welcome to NarBoyfriend!")
st.divider()
col1, col2 = st.columns(2)
col1.image('000050.jpeg', width=300)
col2.markdown(
    """
    Return of the NarBoyfriend! I cannot believe that it has already
    been an entire year. I am so incredibly lucky to have such an
    incredible person by my side. You never fail to make me laugh,
    make me feel loved, and make me the best version of myself. Now that
    one year is already over, I cannot wait to see what our future holds
    in store.

    Love,   
    Jason
    """
)