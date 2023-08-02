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
