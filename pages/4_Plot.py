import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import pyodbc

# CSS for styling the page
page_css = """
<style>
body {
    background-color: #f0f2f6;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

.container {
    max-width: 800px;
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

h2 {
    color: #333333;
    font-size: 20px;
    margin-bottom: 10px;
}

.label {
    font-weight: bold;
    color: #555555;
    margin-bottom: 5px;
    display: block;
}

.input {
    width: 100%;
    padding: 10px;
    margin: 8px 0;
    box-sizing: border-box;
    border: 1px solid #cccccc;
    border-radius: 5px;
    background-color: #f9f9f9;
}

.button {
    width: 100%;
    padding: 10px;
    margin-top: 10px;
    background-color: #4CAF50;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    font-size: 12px;
}

.button:hover {
    background-color: #a4b0d3;
}

.warning {
    color: #ff0000;
    margin-top: 10px;
}

.success {
    color: #4CAF50;
    margin-top: 10px;
}

.info {
    color: #333333;
    margin-top: 10px;
}

.logged-in-message {
    color: #333333;
    font-weight: bold;
    text-align: right;
    margin-top: 10px;
}

.logout-button {
    width: 100%;
    padding: 10px;
    margin-top: 10px;
    background-color: #FF6347;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    font-size: 12px;
}

.logout-button:hover {
    background-color: #a4b0d3;
}
</style>
"""

# Apply the CSS styling
st.markdown(page_css, unsafe_allow_html=True)

col1, col2 = st.columns([3, 1])

if st.session_state.get('username'):
    with col1:
        st.markdown(f'<p class="logged-in-message">Logged in as {st.session_state["username"]}</p>', unsafe_allow_html=True)
    with col2:
        if st.button("Logout", key="logout"):
            st.session_state['username'] = None
            st.session_state['view'] = "login"
            st.success("You have been logged out.")
            st.experimental_rerun()

# Function to fetch userdata from the database
def fetch_userdata(start_date, end_date):
    username = st.session_state['username']
    with get_connection() as conn:
        query = """
        SELECT date, calories_added
        FROM [Userdata]
        WHERE username = ? AND date BETWEEN ? AND ?
        ORDER BY date
        """
        df = pd.read_sql(query, conn, params=(username, start_date, end_date))
    return df

# Function to create connection to MSSQL Server
def get_connection():
    return pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-KCKGKPJ\\MSSQLSERVER01;DATABASE=UserAuth;Trusted_Connection=yes')

def main():# Displaying image
    st.image("images/home_img.jpg")

    st.subheader("Food Nutrition Detection Sytem Using Artificial Intelligence")

    st.write("Our Food Detection Prediction System offers users valuable insights into their dietary habits over time. By plotting the trend of calorie consumption over a specified period, users can visually track changes in their calorie intake, allowing for a deeper understanding of their eating patterns. This feature empowers users to make informed decisions about their diet and lifestyle by providing a clear visualization of their calorie consumption trends. Whether it's monitoring daily, weekly, or monthly calorie intake, Trend Analysis enables users to identify patterns, set goals, and make adjustments to achieve a healthier and more balanced diet. With this tool, users can take proactive steps towards achieving their health and wellness goals, making it an essential component of our Food Detection Prediction System")

    # Date selection widgets
    start_date = st.date_input('Start Date', datetime(2024, 5, 1))
    #end_date = st.date_input('End Date', datetime(2024, 5, 31))
    end_date_radio = st.radio("Select End Date Range:", ["Select End Date", "Last 30 Days", "Last 90 Days", "Last 180 Days"])
    
    if end_date_radio == "Select End Date":
        end_date = st.date_input('End Date', datetime(2024, 5, 31))
    elif end_date_radio == "Last 30 Days":
        end_date = datetime.today()
        start_date = end_date - timedelta(days=30)
    elif end_date_radio == "Last 90 Days":
        end_date = datetime.today()
        start_date = end_date - timedelta(days=90)
    elif end_date_radio == "Last 180 Days":
        end_date = datetime.today()
        start_date = end_date - timedelta(days=180)


    if st.session_state.get('username'):
        with st.form("calorie_input_form"):
            st.write("## Calorie Input")
            calorie_date = st.date_input('Date', datetime.today())
            calorie_amount = st.number_input('Calories', value=0)

            submit_button = st.form_submit_button("Submit")

            if submit_button:
                username = st.session_state['username']
                with get_connection() as conn:
                    cursor = conn.cursor()
                    cursor.execute("INSERT INTO [Userdata] (username, date, calories_added) VALUES (?, ?, ?)", (username, calorie_date, calorie_amount))
                    conn.commit()
                    st.success("Calorie data added successfully!")
    
    # Fetch userdata from the database based on selected date range
    df = fetch_userdata(start_date, end_date)
  # Display userdata table
    if not df.empty:
        st.subheader('User Data')
        st.write(df)
    else:
        st.warning("No data available for the selected date range.")
    # Perform trend analysis and display the plot
    if not df.empty:
        st.subheader('Trend Analysis: Calorie Consumption Over Time')
        fig, trend_classification, mean_calories_per_month = perform_trend_analysis(df)
        st.pyplot(fig)

        # Display classification and mean calories per month
        if trend_classification:
            st.subheader(f'Trend Classification: {trend_classification.capitalize()}')
            st.write(f'Mean Calories : {mean_calories_per_month:.2f}')
    else:
        st.warning("No data available for the selected date range.")

# Function to perform trend analysis
def perform_trend_analysis(df):
    # Calculate mean calorie consumption per month (30 days)
    mean_calories_per_month = df['calories_added'].mean()

    # Determine if the trend is "good" or "bad" based on mean calories per month
    trend_classification = 'good' if mean_calories_per_month <= 100 else 'bad'

    # Create line chart
    fig, ax = plt.subplots()
    ax.plot(df['date'], df['calories_added'], marker='o', linestyle='-')
    ax.set_xlabel('Date')
    ax.set_ylabel('Calories')
    ax.set_title('Calorie Consumption Over Time')
    ax.grid(True)
    return fig, trend_classification, mean_calories_per_month

if st.session_state.get('username'):
    if __name__ == "__main__":
        main()
else:
    st.error("You are not logged in.")
