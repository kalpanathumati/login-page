import streamlit as st

# Set page title and layout
st.set_page_config(page_title="Login Page", layout="centered")

# Custom CSS for styling
st.markdown("""
    <style>
        .login-container {
            background-color: #f0f2f6;
            border-radius: 10px;
            padding: 40px;
            width: 350px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            margin-top: 50px;
            text-align: center;
        }
        .login-header {
            font-size: 24px;
            font-weight: bold;
            color: #4CAF50;
            margin-bottom: 20px;
        }
        .input-field {
            width: 100%;
            padding: 12px;
            margin: 10px 0;
            border-radius: 8px;
            border: 1px solid #ccc;
            font-size: 16px;
        }
        .button {
            width: 100%;
            padding: 12px;
            border-radius: 8px;
            background-color: #4CAF50;
            color: white;
            font-size: 16px;
            border: none;
            cursor: pointer;
        }
        .button:hover {
            background-color: #45a049;
        }
        .footer {
            margin-top: 20px;
            font-size: 12px;
            color: #888;
        }
    </style>
""", unsafe_allow_html=True)

# Create the login form
with st.container():
    st.markdown('<div class="login-container">', unsafe_allow_html=True)
    
    # Header
    st.markdown('<div class="login-header">Welcome Back!</div>', unsafe_allow_html=True)
    
    # User input fields
    username = st.text_input("Username", placeholder="Enter your username", key="username", 
                             label_visibility="collapsed", help="Enter your username", 
                             max_chars=20, key="user_input")
    password = st.text_input("Password", placeholder="Enter your password", type="password", 
                             key="password", label_visibility="collapsed", help="Enter your password")
    
    # Login button
    if st.button("Login", key="login_button", use_container_width=True):
        if username == "admin" and password == "admin":
            st.success("Login successful!")
        elif username == "" or password == "":
            st.warning("Please enter both username and password.")
        else:
            st.error("Incorrect username or password.")

    st.markdown('</div>', unsafe_allow_html=True)

    # Footer
    st.markdown('<div class="footer">Powered by Streamlit</div>', unsafe_allow_html=True)
