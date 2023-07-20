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
    CITY = st.selectbox(
        'Input City',
        ('San Mateo', 'Denver', 'New York City', 'Seattle', 'Boston'))
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
        output = predict_spend_rank(AVG_AMT, CITY, AVG_QUANTITY)
        st.success('The spend rank is {}'.format(output))

        if output == 0:
            st.markdown(low_spender_html, unsafe_allow_html=True)
        elif output == 1:
            st.markdown(high_spender_html, unsafe_allow_html=True)
    

if __name__ =='__main__':
    main()
