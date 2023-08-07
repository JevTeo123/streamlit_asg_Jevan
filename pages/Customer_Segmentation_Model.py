#import libs
import streamlit as st
import pickle
import numpy as np
import pandas as pd
import sklearn
from streamlit_option_menu import option_menu 
model = pickle.load(open('cust_analysis_RF.pkl', 'rb'))
scaler = pickle.load(open('cust_analysis_RF_input.pkl', 'rb'))
input_data = pd.DataFrame(columns = ['CITY', 'GENDER', 'MARITAL_STATUS', 'CHILDREN_COUNT', 'AVG_AMT', 'AVG_QUANTITY', 'FREQ_CATEGORY', 'FREQ_SUBCAT', 'MEAN_PROFIT', 'DAY_DIFF', 'AGE'])
def predict_spend_rank(data):
    #mean = scaler.mean_
    #scale = scaler.scale_
    #input_array_scaled = scaler.transform(data)
    #input_array_scaled = scaler.transform(input)
    st.write("Original Input Data:")
    st.write(data)
    #st.write("Scaled Input Data:")
    #st.write(input_array_scaled)
    prediction = model.predict(data)
    return int(prediction)
def main():
        st.title("Customer Segmentation Model")
        st.markdown("""
        <style>
        .big-font {
            font-size:30px !important;
        }
        </style>
        """, unsafe_allow_html=True)
        # Predictor Variables
        AVG_AMT = 38
        AVG_QUANTITY = 4
        st.markdown('<p class="normal-font">10613:San Mateo, 9122:Denver, 10016:New York City, 7288:Seattle, 9261:Boston</p>', unsafe_allow_html=True)
        CITY = st.number_input('Input City Code', 0, 12000)
        DAY_DIFF = st.number_input('What is the average number of days between your first three transactions?', 0, 1000)
        FREQ_SUBCAT = st.number_input('Input Frequent Subcategory', value = 2)
        MEAN_PROFIT =7.36
        AGE = 50
        GENDER = 1
        CHILDREN_COUNT = 0
        MARITAL_STATUS = 1
        FREQ_CATEGORY = 0

        input_dict = {
            'CITY': CITY,
            'GENDER': GENDER,
            'MARITAL_STATUS': MARITAL_STATUS,
            'CHILDREN_COUNT': CHILDREN_COUNT,
            'AVG_AMT': 38,  # You can adjust these default values
            'AVG_QUANTITY': 4,  # as needed for your application
            'FREQ_CATEGORY': FREQ_CATEGORY,
            'FREQ_SUBCAT': FREQ_SUBCAT,
            'MEAN_PROFIT': MEAN_PROFIT,
            'DAY_DIFF': DAY_DIFF,
            'AGE': AGE
        }
    
        input_data = pd.DataFrame(input_dict, index=[0])
        print("Shape of input_data before scaling:", input_data.shape)
        input_data_scaled = scaler.transform(input_data)
        print("Shape of input_data_scaled:", input_data_scaled.shape) 
        
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
            st.subheader("Scaled Input Data:")
            st.write(input_data_scaled)
    
            if output == 0:
                st.markdown(low_spender_html, unsafe_allow_html=True)
            elif output == 1:
                st.markdown(high_spender_html, unsafe_allow_html=True)
if __name__ == "__main__":
            main()
