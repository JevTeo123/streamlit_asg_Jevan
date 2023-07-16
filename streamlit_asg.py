import streamlit as st
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

st.markdown("""
<style>
.big-font {
    font-size:80px !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="big-font">Customer_RFM Model</p>', unsafe_allow_html=True)
