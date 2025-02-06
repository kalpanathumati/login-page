import streamlit as st

# Function to display login page
def login_page():
    st.title("Login Page")

    # Username and password inputs
    username = st.text_input("Username")
    password = st.text_input("Password", type='password')

    # Check if login button is pressed
    if st.button("Login"):
        if username == "admin" and password == "password123":
            st.success("Login successful!")
            # Redirect to another page or do something after successful login
            st.write("Welcome to the dashboard!")
        else:
            st.error("Invalid username or password")

# Display login page
if __name__ == "__main__":
    login_page()
