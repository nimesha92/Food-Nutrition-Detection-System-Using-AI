import streamlit as st
import tensorflow as tf
import numpy as np
import matplotlib as plt
import pandas as pd  # pip install pandas openpyxl
import plotly.express as px  # pip install plotly-express
import streamlit as st  # pip install streamlit
from PIL import Image
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.dummy import DummyRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error as mse
from math import sqrt
from streamlit_option_menu import option_menu
import matplotlib.pyplot as plt
import time
import requests
import json
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
from streamlit_extras.stylable_container import stylable_container

import streamlit.components.v1 as components
#from streamlit_login_auth_ui.widgets import __login__
import hashlib
import pyodbc
#from courier import Courier


# */""" __login__obj = __login__(auth_token = "courier_auth_token", 
#                     company_name = "Shims",
#                     width = 200, height = 250, 
#                     logout_button_name = 'Logout', hide_menu_bool = False, 
#                     hide_footer_bool = False, 
#                     lottie_url = 'https://assets2.lottiefiles.com/packages/lf20_jcikwtux.json')

# LOGGED_IN = __login__obj.build_login_ui()

# if LOGGED_IN == True:*/



    # Define CSS styles
main_bg = """
    <style>
    body {
        background-image: url('vege.jpg'); 
        background-size: cover;
        background-position: center;
    }
    </style>
    """
st.markdown(main_bg, unsafe_allow_html=True)

sidebar_bg = """
    <style>
    .sidebar .sidebar-content {
        background-color: #f6f1f0;
        color: white;
    }
    </style>
    """





st.markdown(sidebar_bg, unsafe_allow_html=True)
    # Page content
st.title("Food Nutrition Detection Sytem Using Artificial Intelligence")


st.markdown("Food Nutrition Detection  is essential components of a healthy diet. Let’s explore their benefits:")

    # Benefits of fruits and vegetables
st.header("Benefits of Food Nutrition Detection")
st.markdown("- **Nutrient-Rich:** Fruits and vegetables provide a wide range of vitamins, minerals, and antioxidants.")
st.markdown("- **Dietary Fiber:** Both fruits and vegetables are high in dietary fiber, aiding digestion and supporting heart health.")
st.markdown("- **Antioxidants:** Many fruits and vegetables contain antioxidants that help protect against oxidative stress.")

    # System overview
st.header("How the System Works")
st.markdown("Sure! Here's a description of how the Food Nutrition Detection System works,")


    # Image
image_path = "vege.jpg"
st.image(image_path, use_column_width=True)
