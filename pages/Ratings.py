import streamlit as st
import pandas as pd
import plotly.express as px
import pyodbc

# Define CSS styles
main_bg = """
<style>
body {
    background-color: #f0f2f6;
}
</style>
"""
st.markdown(main_bg, unsafe_allow_html=True)

sidebar_bg = """
<style>
.sidebar .sidebar-content {
    background-color: #f63366;
    color: white;
}
</style>
"""
st.markdown(sidebar_bg, unsafe_allow_html=True)

# Function to create connection to MSSQL Server
def get_connection():
    return pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=DESKTOP-KCKGKPJ\\MSSQLSERVER01;'
        'DATABASE=UserAuth;'
        'Trusted_Connection=yes'
    )

# Function to fetch feedback data from database
def fetch_feedback_data():
    conn = get_connection()
    query = "SELECT Rating, Review FROM feedback"
    feedback_data = pd.read_sql(query, conn)
    conn.close()
    return feedback_data

# Displaying image
st.image("images/home_img.jpg")

# Page content
st.title("Food Nutrition Detection Sytem Using Artificial Intelligence")

# Navigation tabs
tabs = ["Ratings and Reviews"]
selected_tab = st.sidebar.radio("Navigation", tabs)

if selected_tab == "Ratings and Reviews":
    st.header("Ratings and Reviews Page")
    st.markdown("Submit your rating and review for the system.")

    # Feedback form
    rating = st.slider("Rating (1-5)", min_value=1, max_value=5, step=1)
    review = st.text_area("Review")

    if st.button("Submit"):
        # Save feedback to database
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO feedback (Rating, Review) VALUES (?, ?)",
            (rating, review)
        )
        conn.commit()
        conn.close()
        st.success("Thank you for your feedback!")

    # Display feedback data
    st.subheader("Feedback Data")
    feedback_data = fetch_feedback_data()
    st.write(feedback_data)

    # Visualize feedback ratings
    st.subheader("Feedback Ratings Chart")
    fig = px.histogram(feedback_data, x='Rating', title='Feedback Ratings Distribution')
    st.plotly_chart(fig)
