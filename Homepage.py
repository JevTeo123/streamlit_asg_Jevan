#import libs
import streamlit as st
import pickle
import numpy as np
import pandas as pd
import sklearn
from streamlit_option_menu import option_menu 

st.set_page_config(
            page_title = "Multipage App",
            page_icon="Home"
)
st.title("Main Page")
st.sidebar.success("Select a page above.")

st.markdown('<p class="big-font">Is your customer a high spender or a low spender?</p>', unsafe_allow_html=True)
        st.markdown('<p class="normal-font">This customer segmentation model seeks to divide customers into distinct groups of individuals which in our case is whether a customer is a high or low spender. This will make it easier tp target specific groups of customers with tailored products so as to hit our high level goals.</p>', unsafe_allow_html=True)
