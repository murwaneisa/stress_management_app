# signup widget
from datetime import datetime
import streamlit as st
# import streamlit_authenticator as stauth
# import styles


class Signup:
    def __init__(self):
        self.first_name = None
        self.last_name = None
        self.gender = None
        self.email = None
        self.program = None
        self.degree = None
        self.password = None
        self.bday = None
        self.study_year = None

    def signup(self):
        gender_options = {
            "F": "Female",
            "M": "Male",
            "X": "Other",
            "NULL": "Prefer not to say"
            }

        # degree_options = ["one", "two"]

        self.first_name = st.text_input("First Name", max_chars=70, key="firstname", autocomplete="given-name")
        self.last_name = st.text_input("Last Name", max_chars=70, key="lastname", autocomplete="family-name")
        self.gender = st.selectbox("Gender", gender_options, format_func=lambda x: gender_options.get(x), key="gender")
        self.email = st.text_input("E-mail", max_chars=70, key="email", autocomplete="email")
        # self.program
        # self.degree = st.selectbox("Degree", degree_options, format_func=lambda x: degree_options.get(x), key="degree")
        self.password = st.text_input("Password", max_chars=70, key="psw", type="password", autocomplete="new-password")
        self.bday = st.date_input("Birthday", value=datetime(1999, 1, 1), min_value=datetime(1900, 1, 1), key="bday")
        self.study_year = st.number_input("Year of studies", min_value=1, max_value=None, value=1, step=None, format=None, key="study-year")

    # def on_confirm(self):
    #     confirm = st.button("Confirm and sign up")
    #     if confirm:
