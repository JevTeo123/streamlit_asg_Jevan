#import libs
import streamlit as st
import pickle
import numpy as np
import sklearn
#from snowflake.snowpark.session import Session
#model = pickle.load(open('model.pkl', 'rb'))

def predict_spend_rank(AVG_AMT, CITY, AVG_QUANTITY):
    input = np.array([[AVG_AMT, CITY, AVG_QUANTITY]]).astype(np.float64)
    prediction = model.predict(input)
    return int(prediction)
def main():
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
    CITY = st.selectbox('What is the city you want to predict customer's spend rank?', ('San Mateo', 'Denver', 'New York City', 'Seattle', 'Boston'))
    

if __name__ =='__main__':
    main()
