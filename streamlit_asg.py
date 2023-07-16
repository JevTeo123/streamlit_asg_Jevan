import streamlit as st
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

st.markdown("""
<style>
.big-font {
    font-size:30px !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="big-font">Customer_RFM Model</p>', unsafe_allow_html=True)
# Predictor Variables
AVG_AMT = st.slider('Input Average Amount', 20, 58)
AVG_QUANTITY = st.slider('Input Average Quantity', 3, 6)
