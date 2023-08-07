#import libs
import streamlit as st
import pickle
import numpy as np
import pandas as pd
import sklearn
from streamlit_option_menu import option_menu 
model = pickle.load(open('cust_analysis_RF.pkl', 'rb'))
scaler = pickle.load(open('cust_analysis_RF_input.pkl', 'rb'))
#input_data = pd.DataFrame(columns = ['CITY', 'GENDER', 'MARITAL_STATUS', 'CHILDREN_COUNT', 'AVG_AMT', 'AVG_QUANTITY', 'FREQ_CATEGORY', 'FREQ_SUBCAT', 'MEAN_PROFIT', 'DAY_DIFF', 'AGE'])
def manual_standardize(data, mean, stds):
    standardized_data = (data - means) / stds
    return standardized_data
def predict_spend_rank(data):
    # new_input_data_reshaped = data.reshape(1, -1)
    # input_array_scaled = scaler.transform(new_input_data_reshaped)
    means = np.array([9396.284536, 0.643758, 0.899028, 1.093952, 38.506258, 4.148999, 0, 1.868661, 1211.778155, 101.773115, 50.184144])
    stds = np.array([1042.916747, 0.663325, 0.937720, 1.381112, 4.216048, 0.408388, 0, 0.425341, 271.497877, 87.299936, 19.275835])
    standardized_data = manual_standardized(data, means, stds)
    st.write("Scaled Input Data:")
    st.write(standardized_data)
    #st.write("Scaled Input Data:")
    #st.write(input_array_scaled)
    prediction = model.predict(standardized_data.reshape(1, -1))
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
            input_data = np.asarray([CITY, GENDER, MARITAL_STATUS, CHILDREN_COUNT, AVG_AMT, AVG_QUANTITY, FREQ_CATEGORY, FREQ_SUBCAT, MEAN_PROFIT, DAY_DIFF, AGE], dtype = np.float64)
            output = predict_spend_rank(input_data)
            st.success('The spend rank is {}'.format(output))
    
            if output == 0:
                st.markdown(low_spender_html, unsafe_allow_html=True)
            elif output == 1:
                st.markdown(high_spender_html, unsafe_allow_html=True)
if __name__ == "__main__":
            main()
