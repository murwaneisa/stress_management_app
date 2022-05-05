import streamlit as st
import database

class Login:

    def user_login(self, email, password):
        db = database.Database()
        login_user = db.login_user(email, password)
        return login_user
    
    def admin_login(self, email, password):
        db = database.Database()
        return db.login_admin(email, password)

    def login_form(self):
        st.subheader("LOGIN")
        with st.form("login_form"):
            email = st.text_input('Email')
            password = st.text_input('Password', type='password')
            submitted = st.form_submit_button("Login")

            if submitted:
                result = Login.user_login(self, email, password)
                return result

    def admin_login_form(self):
        st.subheader("ADMIN LOGIN")
        with st.form("admin_login_form"):
            email = st.text_input('Email')
            password = st.text_input('Password', type='password')
            submitted = st.form_submit_button("Login")
        
            if submitted:
                result = Login.admin_login(self, email, password)
                return result