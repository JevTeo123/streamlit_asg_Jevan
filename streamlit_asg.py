import streamlit as st
#import libs
from snowflake.snowpark.session import Session
import snowflake.snowpark.functions as F
import snowflake.snowpark.types as T
from snowflake.snowpark.window import Window
import preprocessing

import sys
import getpass
import pandas as pd
import numpy as np
from datetime import datetime
from matplotlib import pyplot as plt
import seaborn as sns
from mpl_toolkits import mplot3d 

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import NearestNeighbors
from sklearn.decomposition import PCA
from sklearn import tree

from math import sqrt
from sklearn import metrics
from sklearn.model_selection import cross_val_score, cross_validate
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV

pd.set_option('display.max_columns', None)

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
accountname = getpass.getpass('Enter account name') 
username = getpass.getpass('Enter username')
password = getpass.getpass('Enter password')
connection_parameters = {
    "account": accountname,
    "user": username,
    "password": password,
    "role": "SYSADMIN",
    "database": "FROSTBYTE_TASTY_BYTES",
    "warehouse": "COMPUTE_WH",
    "schema": "RAW_POS"
}

session = Session.builder.configs(connection_parameters).create()
