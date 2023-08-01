#import libs
import streamlit as st
import pickle
import numpy as np
import sklearn
#from snowflake.snowpark.session import Session
#model = pickle.load(open('model.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))


def predict_spend_rank(AVG_AMT, CITY, AVG_QUANTITY, MEAN_PROFIT, AGE, GENDER, FREQ_SUBCAT, CHILDREN_COUNT, MARITAL_STATUS, FREQ_CATEGORY):
    input = np.asarray([[AVG_AMT, CITY, AVG_QUANTITY, MEAN_PROFIT, AGE, GENDER, FREQ_SUBCAT, CHILDREN_COUNT, MARITAL_STATUS, FREQ_CATEGORY]])
    #mean = scaler.mean_
    #scale = scaler.scale_
    input_array_scaled = scaler.fit_transform(input)
    # input_array_scaled = scaler.transform(input)
    st.write(input_array_scaled)
    prediction = model.predict(input_array_scaled)
    return int(prediction)
def main():
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
        output = predict_spend_rank(AVG_AMT, CITY, AVG_QUANTITY, MEAN_PROFIT, AGE, GENDER, FREQ_SUBCAT, CHILDREN_COUNT, MARITAL_STATUS, FREQ_CATEGORY)
        st.success('The spend rank is {}'.format(output))

        if output == 0:
            st.markdown(low_spender_html, unsafe_allow_html=True)
        elif output == 1:
            st.markdown(high_spender_html, unsafe_allow_html=True)
    

if __name__ =='__main__':
    main()
