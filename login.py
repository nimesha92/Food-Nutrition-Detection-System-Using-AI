import streamlit as st

# Define correct username and password
CORRECT_USERNAME = "user"
CORRECT_PASSWORD = "pass"

# Set page background color
st.set_page_config(page_title="Login", page_icon=":lock:", layout="wide", initial_sidebar_state="collapsed")

# Login page
def login():
    st.header("Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("Login"):
            if username == CORRECT_USERNAME and password == CORRECT_PASSWORD:
                st.experimental_set_query_params(logged_in=True)  # Set query parameter
                st.session_state["authentication_status"] = True  # Initialize authentication status
                st.success("Logged in successfully!")
            else:
                st.error("Invalid username or password")

    with col2:
        if st.button("Register"):
            # Add registration functionality here
            st.info("Registration feature coming soon!")

if __name__ == "__main__":
    login()


    
if __name__ == "__main__":
    login()





