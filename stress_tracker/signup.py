import streamlit as st


class SignUp:

    first_name = ""
    last_name = ""
    email = ""
    password = ""
    birth_date = ""
    gender = ""
    program = ""
    degree = ""
    study_year = ""

    def sign_up_ui(self):
        st.subheader("Create an account")

        with st.form("signup_form"):
            col1, col2 = st.columns(2)
            with col1:
                first_name = st.text_input("First Name")
                email = st.text_input('Email')
                birth_date = st.date_input("Date of Birth") # max_date, min_date
                program = st.text_input("Program") # Option
            with col2:
                last_name = st.text_input("Last Name")
                password = st.text_input('Password', type='password')
                gender = st.radio("Gender", ("Male", "Female"))
                degree = st.text_input("Degree") # Options
            study_year = st.text_input("Study Year") # Year (int)
            
            submitted = st.form_submit_button("Sign up")