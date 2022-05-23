from datetime import datetime
import streamlit as st
import streamlit_authenticator as stauth
import global_vars


class Signup:
    def __init__(self, connector):
        self.username = None
        self.first_name = None
        self.last_name = None
        self.gender = None
        self.email = None
        self.program = None
        self.degree = None
        self.password = []
        self.bday = None
        self.study_year = None
        self.connector = connector

    def signup(self):
        self.first_name = st.text_input(
            "First Name", max_chars=70, key="firstname", autocomplete="given-name"
        )
        self.last_name = st.text_input(
            "Last Name", max_chars=70, key="lastname", autocomplete="family-name"
        )
        self.gender = st.selectbox(
            "Gender",
            options=global_vars.gender_options, index=3,
            format_func=lambda x: global_vars.gender_options.get(x),
            key="gender",
        )
        self.email = st.text_input(
            "E-mail", max_chars=70, key="email", autocomplete="email"
        )
        self.program = st.selectbox(
            "Field of your Degree Program", global_vars.course_options, key="program"
        )
        self.degree = st.selectbox(
            "Level of Study", global_vars.degree_options, key="degree"
        )
        self.bday = st.date_input(
            "Birthday",
            value=datetime(1995, 1, 1),
            min_value=datetime(1900, 1, 1),
            key="bday",
        )
        self.study_year = st.number_input(
            "Year of studies",
            min_value=1,
            max_value=10,
            value=1,
            key="study-year",
        )
        self.username = st.text_input(
            "Username", max_chars=70, autocomplete="username"
        )
        self.password.append((st.text_input(
            "Password",
            max_chars=70,
            key="psw",
            type="password",
            autocomplete="new-password",
        )))

    def on_confirm(self):
        if st.button("Confirm and sign up"):
            values = {}
            values["user_username"] = [self.username,"str"]
            values["user_firstname"] =[self.first_name,"str"]
            values["user_lastname"] = [self.last_name,"str"]
            values["user_gender"] = [self.gender,"str"]
            values["user_email"] = [self.email,"str"]
            values["user_program"] = [self.program,"str"]
            values["user_degree"] = [self.degree,"str"]
            values["user_password"] = [stauth.Hasher(self.password).generate()[0],"str"]
            values["user_dob"] = [self.bday,"str"]
            values["user_studystart"] = [self.study_year,"str"]

            print(values)

            self.connector.insertData(values, "user")

