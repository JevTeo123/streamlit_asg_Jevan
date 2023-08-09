#import libs
import streamlit as st
import pickle
import numpy as np
import pandas as pd
import sklearn
import altair as alt
from streamlit_option_menu import option_menu 
model = pickle.load(open('cust_analysis_RF_Jevan.pkl', 'rb'))
scaler = pickle.load(open('cust_analysis_RF_input.pkl', 'rb'))
#input_data = pd.DataFrame(columns = ['CITY', 'GENDER', 'MARITAL_STATUS', 'CHILDREN_COUNT', 'AVG_AMT', 'AVG_QUANTITY', 'FREQ_CATEGORY', 'FREQ_SUBCAT', 'MEAN_PROFIT', 'DAY_DIFF', 'AGE'])
with st.sidebar:
    selected = option_menu(
        menu_title="Main Menu",
        options=["Home", "Customer Segmentation Model", "Distinct Insights"],
        icons=["house", "person-circle", "pie-chart"]
    )
df = pd.read_csv('rest_customer_us_Jevan.csv')
high_spender_df = df.loc[df['SPEND_RANK'] == 1]
low_spender_df = df.loc[df['SPEND_RANK'] == 0]
if selected == "Home":
    st.title("Welcome to Jevan's streamlit app!")
    st.sidebar.success("Select a page above.")
    
    st.subheader('Is your customer a high spender 💰 or a low spender 👎?')
    st.markdown('<p class="normal-font">This customer segmentation model seeks to divide customers into distinct groups of individuals which in our case is whether a customer is a high or low spender. This will make it easier to target specific groups of customers with tailored products so as to hit our high level goals.</p>', unsafe_allow_html=True)

if selected == "Customer Segmentation Model":
    def manual_standardize(data, means, stds):
        standardized_data = (data - means) / stds
        return standardized_data
    def predict_spend_rank(data):
        # new_input_data_reshaped = data.reshape(1, -1)
        # input_array_scaled = scaler.transform(new_input_data_reshaped)
        means = np.array([9396.284536, 0.643758, 0.899028, 1.093952, 38.506258, 4.148999, 1.868661, 1211.778155, 101.773115, 57.798256, 50.184144])
        stds = np.array([1042.916747, 0.663325, 0.937720, 1.381112, 4.216048, 0.408388, 0.425341, 271.497877, 87.299936, 10.638129, 19.275835])
        standardized_data = manual_standardize(data, means, stds)
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
            DAY_DIFF = st.number_input('Input customer\'s average number of days between their first three transactions', 0, 1000)
            #FREQ_SUBCAT = st.number_input('Input Frequent Subcategory', value = 2)
            FREQ_SUBCAT_options = st.selectbox("Input customer's frequent subcategory of items that they order", list(freq_subcat_mapping.keys()))
            FREQ_SUBCAT = freq_subcat_mapping[FREQ_SUBCAT_options]            #FREQ_SUBCAT = 2
            MEAN_PROFIT = 7.36
            AGE = 50
            GENDER = 1
            CHILDREN_COUNT = 0
            MARITAL_STATUS = 1
            TOTAL_TRANS = st.number_input('Input total number transactions made by customer', 0, 100)
            
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
            #Filter df by inputs
            specific_condition_filter = (
                (df['FREQ_SUBCAT'] == FREQ_SUBCAT) &
                (df['DAY_DIFF'] == DAY_DIFF) &
                (df['TOTAL_TRANS'] == TOTAL_TRANS)
            )
            filtered_df = df[specific_condition_filter]
            if(filtered_df.empty):
                fallback_condition1 = (
                    (df['FREQ_SUBCAT'] == FREQ_SUBCAT) &
                    (df['DAY_DIFF'] == DAY_DIFF)
                )
                fallback_condition2 = (
                    (df['FREQ_SUBCAT'] == FREQ_SUBCAT) &
                    (df['TOTAL_TRANS'] == TOTAL_TRANS)
                )
                fallback_condition3 = (
                    (df['DAY_DIFF'] == DAY_DIFF) &
                    (df['TOTAL_TRANS'] == TOTAL_TRANS)
                )
                filtered_df = df[fallback_condition1 | fallback_condition2 | fallback_condition3]
                
            if st.button("Predict the spend rank of the customer🏆"):
                input_data = np.asarray([CITY, GENDER, MARITAL_STATUS, CHILDREN_COUNT, AVG_AMT, AVG_QUANTITY, FREQ_SUBCAT, MEAN_PROFIT, DAY_DIFF, TOTAL_TRANS, AGE], dtype = np.float64)
                output = predict_spend_rank(input_data)
                st.success('The spend rank is {}'.format(output))
        
                if output == 0:
                    st.markdown(low_spender_html, unsafe_allow_html=True)
                    gender_modes = filtered_df['GENDER'].mode()
                    city_modes = filtered_df['CITY'].mode()
                    marital_status_modes = filtered_df['MARITAL_STATUS'].mode()
                    gender = gender_modes.values[0] if not gender_modes.empty else "Unknown"
                    city = city_modes.values[0] if not city_modes.empty else "Unknown"
                    marital_status = marital_status_modes.values[0] if not marital_status_modes.empty else "Unknown"
                    gender_mapping = {
                        0:'Female',
                        1: 'Male',
                        2: 'Undisclosed'
                    }
                    marital_status_mapping = {
                        0 : 'Single',
                        1 : 'Married',
                        2 : 'Divorced/Seperated',
                        3 : 'Undisclosed'
                    }
                    city_mapping = {
                        10613 : 'San Mateo',
                        10016 : 'New York City',
                        9261 : 'Boston',
                        9122 : 'Denver',
                        7288 : 'Seattle'
                    }
                    gender_label = gender_mapping.get(gender)
                    city_label = city_mapping.get(city)
                    marital_status_label = marital_status_mapping.get(marital_status)
                    formatted_insight = "Based on the input, Customer is most likely to be a {} and lives in {} and is generally {}.".format(gender_label, city_label, marital_status_label) 
                    st.subheader("Customer Behavioural Insights🔍:")
                    st.write(formatted_insight)
                elif output == 1:
                    st.markdown(high_spender_html, unsafe_allow_html=True)
                    gender_modes = filtered_df['GENDER'].mode()
                    city_modes = filtered_df['CITY'].mode()
                    marital_status_modes = filtered_df['MARITAL_STATUS'].mode()
                    gender = gender_modes.values[0] if not gender_modes.empty else "Unknown"
                    city = city_modes.values[0] if not city_modes.empty else "Unknown"
                    marital_status = marital_status_modes.values[0] if not marital_status_modes.empty else "Unknown"
                    gender_mapping = {
                        0:'Female',
                        1: 'Male',
                        2: 'Undisclosed'
                    }
                    marital_status_mapping = {
                        0 : 'Single',
                        1 : 'Married',
                        2 : 'Divorced/Seperated',
                        3 : 'Undisclosed'
                    }
                    city_mapping = {
                        10613 : 'San Mateo',
                        10016 : 'New York City',
                        9261 : 'Boston',
                        9122 : 'Denver',
                        7288 : 'Seattle'
                    }
                    gender_label = gender_mapping.get(gender)
                    city_label = city_mapping.get(city)
                    marital_status_label = marital_status_mapping.get(marital_status)
                    formatted_insight = "Based on the input, Customer is most likely to be a {} and lives in {} and is generally {}.".format(gender_label, city_label, marital_status_label) 
                    st.subheader("Customer Behavioural Insights🔍:")
                    st.write(formatted_insight)
    if __name__ == "__main__":
                main()
if selected == "Distinct Insights":
    st.title("Distinct Insights 📈")
    st.markdown('<p class="big-font">Average Total Transaction by high or low spender</p>', unsafe_allow_html=True)
    spender_avg_trans = df.groupby(['SPEND_RANK'])['TOTAL_TRANS'].mean()
    st.bar_chart(spender_avg_trans)
    text = '<p class="normal-font">Customers who are high spenders💰 typically have an average total number of transactions of <span style="color: green;">63 and above</span> while customers who are low spenders 👎 have an average total number of transactions of <span style="color: red;">51 and below</span>.</p>'
    st.markdown(text, unsafe_allow_html=True)
    day_diff_average = df.groupby(['SPEND_RANK'])['DAY_DIFF'].mean()
    st.markdown('<p class="big-font">Average difference of days in first 3 transactions by high or low spender</p>', unsafe_allow_html=True)
    st.bar_chart(day_diff_average)
    text1 = '<p class="normal-font">Customers who are high spenders💰 typically have an average difference of days in first 3 transactions of <span style="color: green;">76 days and below</span> while customers who are low spenders 👎 have an average total number of transactions of <span style="color: red;">127 days and above</span>.</p>'
    st.markdown(text1, unsafe_allow_html = True)
    subcategory_mapping = {
    0: "Cold Option",
    1: "Warm Option",
    2: "Hot Option"
    }
    # Group data by SPEND_RANK and FREQ_SUBCAT and count occurrences
    spender_freq_subcat_count = df.groupby(['SPEND_RANK', 'FREQ_SUBCAT']).size().reset_index(name='COUNT')
    
    # Update the FREQ_SUBCAT values to their corresponding string labels
    spender_freq_subcat_count['FREQ_SUBCAT_LABEL'] = spender_freq_subcat_count['FREQ_SUBCAT'].map(subcategory_mapping)
    
    # Create a clustered column chart using Altair
    chart = alt.Chart(spender_freq_subcat_count).transform_calculate(
        FREQ_SUBCAT_LABEL='datum.FREQ_SUBCAT_LABEL'
    ).mark_bar().encode(
        x=alt.X('FREQ_SUBCAT_LABEL:N', title='Frequent Subcategory'),
        y=alt.Y('COUNT:Q', title='Count'),
        color=alt.Color('SPEND_RANK:N', scale=alt.Scale(domain=['0', '1'], range=['red', 'green']), legend=alt.Legend(title='Spend Rank'))
    ).properties(
        width=600,
        height=400,
        title="Count of High💰 and Low👎 Spenders Based on Frequent Subcategory"
    )
    
    # Display the chart in Streamlit
    st.altair_chart(chart, use_container_width=True)

    
    text = '<p class="normal-font">In general, being a high spender💰 or low spender👎 does not affect the choice of subcategory of items they are purchasing. The subcategory of items with the most count of people buying would be the <span style="color: green;">hot option</span>☕.</p>'
    st.markdown(text, unsafe_allow_html=True)
