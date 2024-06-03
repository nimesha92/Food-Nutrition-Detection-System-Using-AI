
import streamlit as st
import pandas as pd
import plotly.express as px

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

# Data for feedbacks (dummy data for demonstration)
feedback_data = pd.DataFrame({
    'Rating': [4, 5, 3, 5, 4],
    'Review': ["Great app!", "Love it!", "Could be better", "Awesome", "Good job!"]
})


# Displaying image
st.image("images/home_img.jpg")
# Page content
st.title("FRUITS & VEGETABLES RECOGNITION SYSTEM")

# Navigation tabs
tabs = [ "Ratings and Reviews"]
selected_tab = st.sidebar.radio("Navigation", tabs)



if selected_tab == "Ratings and Reviews":
    st.header("Ratings and Reviews Page")
    st.markdown("Submit your rating and review for the system.")

    # Feedback form
    rating = st.slider("Rating (1-5)", min_value=1, max_value=5, step=1)
    review = st.text_area("Review")

    if st.button("Submit"):
     
        st.success("Thank you for your feedback!")

    # Display feedback data
    st.subheader("Feedback Data")
    st.write(feedback_data)

    # Visualize feedback ratings
    st.subheader("Feedback Ratings Chart")
    fig = px.histogram(feedback_data, x='Rating', title='Feedback Ratings Distribution')
    st.plotly_chart(fig)
