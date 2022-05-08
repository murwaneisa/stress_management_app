# signup widget
from datetime import datetime
import streamlit as st
import global_vars
# import streamlit_authenticator as stauth
# import styles


class Signup:
    def __init__(self, connector):
        self.first_name = None
        self.last_name = None
        self.gender = None
        self.email = None
        self.program = None
        self.degree = None
        self.password = None
        self.bday = None
        self.study_year = None
        self.connector = connector


    def signup(self):
        self.first_name = st.text_input("First Name", max_chars=70, key="firstname", autocomplete="given-name")
        self.last_name = st.text_input("Last Name", max_chars=70, key="lastname", autocomplete="family-name")
        self.gender = st.selectbox("Gender", global_vars.gender_options, format_func=lambda x: global_vars.gender_options.get(x), key="gender")
        self.email = st.text_input("E-mail", max_chars=70, key="email", autocomplete="email")
        self.program = st.selectbox("Field of your Degree Program",global_vars.course_options, key="program")
        self.degree = st.selectbox("Level of Study", global_vars.degree_options, key="degree")
        self.password = st.text_input("Password", max_chars=70, key="psw", type="password", autocomplete="new-password")
        self.bday = st.date_input("Birthday", value=datetime(1995, 1, 1), min_value=datetime(1900, 1, 1), key="bday")
        self.study_year = st.number_input("Year of studies", min_value=1, max_value=None, value=1, step=None, format=None, key="study-year")

    def on_confirm(self):
        confirm = st.button("Confirm and sign up")
        if confirm:
            self.connector.insert_user(self.first_name,
                                       self.last_name,
                                       self.gender,
                                       self.email,
                                       self.program,
                                       self.level,
                                       self.password,
                                       self.bday,
                                       self.study_year)
        return self.email, self.password
