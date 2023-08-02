#import libs
import streamlit as st
import pickle
import numpy as np
import pandas as pd
import sklearn
from streamlit_option_menu import option_menu 
#from snowflake.snowpark.session import Session
#model = pickle.load(open('model.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))
input_data = pd.DataFrame(columns = ['CITY', 'GENDER', 'MARITAL_STATUS', 'CHILDREN_COUNT', 'AVG_AMT', 'AVG_QUANTITY', 'FREQ_CATEGORY', 'FREQ_SUBCAT', 'MEAN_PROFIT', 'AGE'])
def predict_spend_rank(data):
    #mean = scaler.mean_
    #scale = scaler.scale_
    input_array_scaled = scaler.transform(data)
    # input_array_scaled = scaler.transform(input)
    st.write("Original Input Data:")
    st.write(data)
    st.write("Scaled Input Data:")
    st.write(input_array_scaled)
    prediction = model.predict(input_array_scaled)
    return int(prediction)
def main():
    selected = option_menu(
            menu_title=None,
            options=["Home", "Customer Segmentation Model"],
            icons=["house", "person-square"],
            default_index = 0,
            orientation="horizontal",
            menu_icon="cast",
        )
    if selected == "Home":
            st.title(f"You have selected {selected}")
    if selected == "Customer Segmentation Model":
            st.title(f"You have selected {selected}")
    st.markdown("""
    <style>
    .big-font {
        font-size:30px !important;
    }
    </style>
    """, unsafe_allow_html=True)
    st.markdown('<p class="big-font">Is your customer a high spender or a low spender?</p>', unsafe_allow_html=True)
    st.markdown('<p class="normal-font">This customer segmentation model seeks to divide customers into distinct groups of individuals which in our case is whether a customer is a high or low spender. This will make it easier tp target specific groups of customers with tailored products so as to hit our high level goals.</p>', unsafe_allow_html=True)
    # Predictor Variables
    AVG_AMT = st.number_input('Input Average Amount', 20, 58)
    AVG_QUANTITY = st.number_input('Input Average Quantity', 3, 6)
    st.markdown('<p class="normal-font">0:San Mateo, 1:Denver, 2:New York City, 3:Seattle, 4:Boston</p>', unsafe_allow_html=True)
    CITY = st.slider('Input City Code', 0, 5)
    MEAN_PROFIT = st.number_input('Input Mean Profit', 7.36)
    AGE = st.number_input('Input Age', 50)
    GENDER = st.number_input('Input Gender', 1)
    FREQ_SUBCAT = st.number_input('Input Frequent Subcategory', value = 2)
    CHILDREN_COUNT = st.number_input('Input Children Count', value = 0)
    MARITAL_STATUS = st.number_input('Input Marital Status', value = 1)
    FREQ_CATEGORY = st.number_input('Input Frequent Category', value = 0)

    input_data.loc[0] = [CITY, GENDER, MARITAL_STATUS, CHILDREN_COUNT, AVG_AMT, AVG_QUANTITY, FREQ_CATEGORY, FREQ_SUBCAT, MEAN_PROFIT, AGE]
    
    
    low_spender_html="""
        <div style="background-color:#80ff80; padding:10px >
        <h2 style="color:white;text-align:center;"> The customer is a low spender</h2>
        </div>
    """
    high_spender_html="""
        <div style="background-color:#F4D03F; padding:10px >
        <h2 style="color:white;text-align:center;"> The customer is a high spender</h2>
        </div>
    """
    
    if st.button("Predict the spend rank of the customer"):
        output = predict_spend_rank(input_data)
        st.success('The spend rank is {}'.format(output))

        if output == 0:
            st.markdown(low_spender_html, unsafe_allow_html=True)
        elif output == 1:
            st.markdown(high_spender_html, unsafe_allow_html=True)
    

