import streamlit as st
from streamlit_option_menu import option_menu
import tensorflow as tf
import numpy as np
import pandas as pd  # pip install pandas openpyxl
import plotly.express as px  # pip install plotly-express
from PIL import Image
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.dummy import DummyRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error as mse
from math import sqrt
import matplotlib.pyplot as plt
import time
import requests
import json
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
from streamlit_extras.stylable_container import stylable_container
import pyodbc
import os
import hashlib


# CSS for styling the login page
login_page_css = """
<style>
body {
    background-color: #f0f2f6;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

.container {
    max-width: 400px;
    margin: auto;
    padding: 20px;
    border-radius: 10px;
    background-color: #ffffff;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    margin-top: 50px;
}

h1 {
    text-align: center;
    color: #333333;
    font-size: 24px;
    margin-bottom: 20px;
}

label {
    font-weight: bold;
    color: #555555;
    margin-bottom: 5px;
    display: block;
}

input[type="text"], input[type="password"] {
    width: 100%;
    padding: 10px;
    margin: 8px 0;
    box-sizing: border-box;
    border: 1px solid #cccccc;
    border-radius: 5px;
    background-color: #f9f9f9;
}

.button-container {
    display: flex;
    justify-content: flex-end;
    gap: 10px;
    margin-top: 10px;
}

button {
    padding: 8px;
    background-color: #5dbea3;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    font-size: 12px;
}

button:hover {
    background-color: #a4b0d3;
}

.error-message {
    color: #ff0000;
    margin-top: 10px;
}

.success-message {
    color: #4CAF50;
    margin-top: 10px;
}

.info-message {
    color: #333333;
    margin-top: 10px;
}

.logged-in-message {
    color: #333333;
    font-weight: bold;
    text-align: right;
    margin-top: 10px;
}
</style>
"""

# Apply the CSS styling
st.markdown(login_page_css, unsafe_allow_html=True)

# Function to create connection to MSSQL Server
def get_connection():
    return pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-KCKGKPJ\\MSSQLSERVER01;DATABASE=UserAuth;Trusted_Connection=yes')

# Function to test database connection
def test_connection():
    try:
        with get_connection():
            return True
    except Exception as e:
        print("Connection failed:", e)
        return False

# Function to create user table if not exists
def create_user_table(conn):
    with conn.cursor() as cursor:
        cursor.execute("""
            IF NOT EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[Users]') AND type in (N'U'))
            BEGIN
                CREATE TABLE [Users] (
                    id INT PRIMARY KEY IDENTITY,
                    username NVARCHAR(50) UNIQUE NOT NULL,
                    password NVARCHAR(64) NOT NULL,
                    salt NVARCHAR(64) NOT NULL
                )
            END
        """)
        conn.commit()

# Function to check if user exists
def check_user(conn, username):
    with conn.cursor() as cursor:
        cursor.execute("SELECT COUNT(*) FROM [Users] WHERE username = ?", (username,))
        return cursor.fetchone()[0] > 0

# Function to register user
def register_user(conn, username, password):
    salt = os.urandom(32)  # Generate a random salt
    hashed_password = hashlib.sha256(password.encode('utf-8') + salt).hexdigest()
    with conn.cursor() as cursor:
        cursor.execute("INSERT INTO [Users] (username, password, salt) VALUES (?, ?, ?)", (username, hashed_password, salt.hex()))
        conn.commit()

# Function to authenticate user
def authenticate_user(conn, username, password):
    with conn.cursor() as cursor:
        cursor.execute("SELECT password, salt FROM [Users] WHERE username = ?", (username,))
        result = cursor.fetchone()
        if result:
            stored_password = result[0]
            salt = bytes.fromhex(result[1])  # Convert hex string back to bytes
            hashed_password = hashlib.sha256(password.encode('utf-8') + salt).hexdigest()
            return stored_password == hashed_password
        return False

# Display login form
with st.container():
    if test_connection():
        with get_connection() as conn:
            create_user_table(conn)

            # Initialize session state variables
            if 'username' not in st.session_state:
                st.session_state['username'] = None
            if 'view' not in st.session_state:
                st.session_state['view'] = "login"

            # Display login, logout, and registration buttons in the top-right corner
            col1, col2 = st.columns([3, 1])

            if st.session_state['username']:
                with col1:
                    st.markdown(f'<p class="logged-in-message">Logged in as {st.session_state["username"]}</p>', unsafe_allow_html=True)
                with col2:
                    if st.button("Logout", key="logout"):
                        st.session_state['username'] = None
                        st.session_state['view'] = "login"
                        st.success("You have been logged out.")
                        st.experimental_rerun()  # Rerun the app to reflect changes
            else:
                if st.session_state['view'] == "login":
                    login_username = st.text_input("Username", key="login_username")
                    login_password = st.text_input("Password", type="password", key="login_password")
                    # buttons_html = """
                    # # <div class="button-container">
                    # #     <button onclick="document.getElementById('login_button').click()">Login</button>
                    # #     <button onclick="document.getElementById('show_register').click()">Register Here</button>
                    # # </div>
                    # # """
                    #st.markdown(buttons_html, unsafe_allow_html=True)
                    if st.button("Login", key="login_button"):
                        if authenticate_user(conn, login_username, login_password):
                            st.session_state['username'] = login_username
                            st.session_state['view'] = "content"
                            st.success("Successfully logged in!")
                            st.experimental_rerun()  # Rerun the app to reflect changes
                        else:
                            st.error("Invalid username or password")
                    if st.button("Register Here", key="show_register"):
                        st.session_state['view'] = "register"

                elif st.session_state['view'] == "register":
                    reg_username = st.text_input("Register Username", key="reg_username")
                    reg_password = st.text_input("Register Password", type="password", key="reg_password")
                    confirm_password = st.text_input("Confirm Password", type="password", key="confirm_password")
                    if st.button("Register", key="register_button"):
                        if reg_password == confirm_password:
                            if not check_user(conn, reg_username):
                                register_user(conn, reg_username, reg_password)
                                st.success("Registration successful. You can now login.")
                                st.session_state['view'] = "login"
                            else:
                                st.error("Username already exists")
                        else:
                            st.error("Passwords do not match")
                    if st.button("Back to Login", key="back_to_login"):
                        st.session_state['view'] = "login"
                        
            # Your content goes here
            if st.session_state['username']:
                def model_prediction(test_image):
                    model = tf.keras.models.load_model("trained_model.h5")
                    image = tf.keras.preprocessing.image.load_img(test_image, target_size=(64, 64))
                    input_arr = tf.keras.preprocessing.image.img_to_array(image)
                    input_arr = np.array([input_arr])  # Convert single image to batch
                    predictions = model.predict(input_arr)
                    return np.argmax(predictions)  # Return index of max element


                if st.session_state["username"]:
                    image_path = "images/home_img.jpg"
                    st.image(image_path)
                    st.header("Model Prediction")
                    test_image = st.file_uploader("Choose an Image:")
                    if(st.button("Show Image")):
                        try:
                            st.image(test_image, use_column_width=True)
                        except Exception as e:
                            st.error("Please select an image first")

                    # Predict button
                    if(st.button("Predict")):
                        try:
                            st.snow()
                            st.write("Our Prediction")
                            result_index = model_prediction(test_image)
                            # Reading Labels
                            with open("labels.txt") as f:
                                content = f.readlines()
                            label = [i.strip() for i in content]
                            st.success(f"Model is Predicting it's a {label[result_index]}")
                        except Exception as e:
                            st.error("Please select an image first")

    else:
        st.error("Failed to establish connection to the database. Please check your database settings.")
