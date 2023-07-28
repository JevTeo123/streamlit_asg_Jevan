#import libs
import streamlit as st
import pickle
import numpy as np
import sklearn
#from snowflake.snowpark.session import Session
model = pickle.load(open('model.pkl', 'rb'))

def predict_spend_rank(AVG_AMT, CITY, AVG_QUANTITY, MEAN_PROFIT, AGE, GENDER, FREQ_SUBCAT, CHILDREN_COUNT, MARITAL_STATUS, FREQ_CATEGORY):
    input = np.asarray([[AVG_AMT, CITY, AVG_QUANTITY, MEAN_PROFIT, AGE, GENDER, FREQ_SUBCAT, CHILDREN_COUNT, MARITAL_STATUS, FREQ_CATEGORY]])
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
    st.markdown('<p class="big-font">Is your customer a high spender or a low spender?</p>', unsafe_allow_html=True)
    # Predictor Variables
    AVG_AMT = st.slider('Input Average Amount', 20, 58)
    AVG_QUANTITY = st.slider('Input Average Quantity', 3, 6)
    st.markdown('<p class="normal-font">0:San Mateo, 1:Denver, 2:New York City, 3:Seattle, 4:Boston</p>', unsafe_allow_html=True)
    CITY = st.slider('Input City Code', 0, 5)
    MEAN_PROFIT = st.slider('Input Mean Profit', 7.36)
    AGE = st.slider('Input Age', 50)
    GENDER = st.slider('Input Gender', 1)
    FREQ_SUBCAT = st.slider('Input Frequent Subcategory', 2)
    CHILDREN_COUNT = st.slider('Input Children Count', 0)
    MARITAL_STATUS = st.slider('Input Marital Status', 1)
    FREQ_CATEGORY = st.slider('Input Frequent Category', 0)
    
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
