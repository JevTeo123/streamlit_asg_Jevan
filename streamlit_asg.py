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
