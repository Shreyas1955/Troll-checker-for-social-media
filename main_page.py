import streamlit as st
from login_page import login_page
from user_page import user_page
from admin_page import admin_page

def main():
    if st.session_state.get("logged_in"):
        if st.session_state["role"] == "user":
            user_page()
        elif st.session_state["role"] == "admin":
            admin_page()
    else:
        login_page()

if __name__ == "__main__":
    main()
