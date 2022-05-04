# full credit to M Khorasani for streamlit_authenticator

import streamlit as st
import streamlit_authenticator as stauth
from user_profile import user_profile

# page config
st.set_page_config(
    page_title="Stress Tracker",
    page_icon="🐛",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        "Get Help": "https://www.github.com/",
        "Report a bug": "https://www.github.com/",
        "About": "",
    },
)


# styles
day_header_style = '<p style="color:Green; font-size: 20px;">'

name = "Murwan Eisa"
user = "meisa"
passw = "welcome123"

# users
names = [name]
usernames = [user]
passwords = [passw]

# encrypt passwords
hashed_passwords = stauth.Hasher(passwords).generate()


st.title("STRESS TRACKER")

authenticator = stauth.Authenticate(
    names,
    usernames,
    hashed_passwords,
    "some_cookie_name",
    "some_signature_key",
    cookie_expiry_days=30,
)


name, authentication_status, username = authenticator.login("Login", "main")


if authentication_status:
    user_profile()
elif authentication_status is False:
    st.error("Username/password is incorrect")
elif authentication_status is None:
    st.warning("Please enter your username and password")
