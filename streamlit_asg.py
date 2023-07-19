#import libs
import streamlit as st
import pickle
import numpy as np

pd.set_option('display.max_columns', None)

st.markdown("""
<style>
.big-font {
    font-size:30px !important;
}
</style>
""", unsafe_allow_html=True)

model = pickle.load(open('model.pkl', 'rb'))

st.markdown('<p class="big-font">Customer_RFM Model</p>', unsafe_allow_html=True)
# Predictor Variables
AVG_AMT = st.slider('Input Average Amount', 20, 58)
AVG_QUANTITY = st.slider('Input Average Quantity', 3, 6)
accountname = getpass.getpass('Enter account name') 
username = getpass.getpass('Enter username')
password = getpass.getpass('Enter password')
