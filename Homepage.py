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
with st.sidebar:
    selected = option_menu(
        menu_title="Main Menu",
        options=["Home", "Customer Segmentation Model", "LIME Explanation on Model"],
        icons=["house", "person-circle", "pie-chart"]
    )
if selected == "Home":
    st.title("Welcome to Jevan's streamlit app!")
    st.sidebar.success("Select a page above.")
    
    st.markdown('<p class="big-font">Is your customer a high spender 💰 or a low spender 👎?</p>', unsafe_allow_html=True)
    st.markdown('<p class="normal-font">This customer segmentation model seeks to divide customers into distinct groups of individuals which in our case is whether a customer is a high or low spender. This will make it easier to target specific groups of customers with tailored products so as to hit our high level goals.</p>', unsafe_allow_html=True)

if selected == "Customer Segmentation Model":
    def manual_standardize(data, means, stds):
        standardized_data = (data - means) / stds
        return standardized_data
    def predict_spend_rank(data):
        # new_input_data_reshaped = data.reshape(1, -1)
        # input_array_scaled = scaler.transform(new_input_data_reshaped)
        means = np.array([9396.284536, 0.643758, 0.899028, 1.093952, 38.506258, 4.148999, 1.868661, 1211.778155, 101.773115, 50.184144])
        stds = np.array([1042.916747, 0.663325, 0.937720, 1.381112, 4.216048, 0.408388, 0.425341, 271.497877, 87.299936, 19.275835])
        standardized_data = manual_standardize(data, means, stds)
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
            freq_subcat_mapping = {
                "Cold Option": 0,
                "Warm Option": 1,
                "Hot Option": 2
            }
            AVG_AMT = 38
            AVG_QUANTITY = 4
            CITY = 10016 #Used the city of San Mateo as it has the highest sales, more room to work on
            DAY_DIFF = st.number_input('What is the average number of days between your first three transactions?', 0, 1000)
            #FREQ_SUBCAT = st.number_input('Input Frequent Subcategory', value = 2)
            FREQ_SUBCAT_options = st.selectbox("What is the frequent subcategory of items you order?", list(freq_subcat_mapping.keys()))
            FREQ_SUBCAT = freq_subcat_mapping[FREQ_SUBCAT_options]
            MEAN_PROFIT =7.36
            AGE = st.number_input("What is your age?", 0, 150)
            GENDER = 1
            CHILDREN_COUNT = 0
            MARITAL_STATUS = 1
            
            low_spender_html="""
                <div style="background-color:#80ff80; padding:10px >
                <h2 style="color:white;text-align:center;"> The customer is a low spender 👎</h2>
                </div>
            """
            high_spender_html="""
                <div style="background-color:#F4D03F; padding:10px >
                <h2 style="color:white;text-align:center;"> The customer is a high spender 💰</h2>
                </div>
            """
            df = pd.read_csv('rest_customer_us.csv')
            high_spender_df = df.loc[df['SPEND_RANK'] == 1]
            st.write(high_spender_df.head())
            if st.button("Predict the spend rank of the customer"):
                input_data = np.asarray([CITY, GENDER, MARITAL_STATUS, CHILDREN_COUNT, AVG_AMT, AVG_QUANTITY, FREQ_SUBCAT, MEAN_PROFIT, DAY_DIFF, AGE], dtype = np.float64)
                output = predict_spend_rank(input_data)
                st.success('The spend rank is {}'.format(output))
        
                if output == 0:
                    st.markdown(low_spender_html, unsafe_allow_html=True)
                elif output == 1:
                    st.markdown(high_spender_html, unsafe_allow_html=True)
    if __name__ == "__main__":
                main()
if selected == "LIME Explanation on Model":
    explainer = lime.lime_tabular.LimeTabularExplainer()
