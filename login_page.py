import streamlit as st
import mysql.connector

#Function to connect to MySQL database
def connect_db():
    connection = mysql.connector.connect(
        host="localhost",
        user="root", 
        password="",  
        database="social_media_platform"
    )
    return connection

#Authentication function
def authenticate_user(username, password):
    conn = connect_db()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    return user

#Main function for login page
def login_page():
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        user = authenticate_user(username, password)
        if user:
            st.session_state["username"] = user["username"]
            st.session_state["role"] = user["role"]
            st.session_state.logged_in = True
        else:
            st.error("Invalid credentials")

if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
