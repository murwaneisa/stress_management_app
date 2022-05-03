# full credit to M Khorasani for streamlit_authenticator

import streamlit as st

# page config
st.set_page_config(
     page_title="Stress Tracker",
     page_icon="🐛",
     layout="wide",
     initial_sidebar_state="expanded",
     menu_items={
         'Get Help': 'https://www.github.com/',
         'Report a bug': "https://www.github.com/",
         'About': ""
     }
 )

import streamlit_authenticator as stauth
import weekly_log
import mood_log
# import mysql.connector


# Initialize connection.
# Uses st.experimental_singleton to only run once.
# @st.experimental_singleton
# def init_connection():
#     return mysql.connector.connect(**st.secrets["mysql"])

# conn = init_connection()

# Perform query.
# Uses st.experimental_memo to only rerun when the query changes or after 10 min.
# @st.experimental_memo(ttl=600)
# def run_query(query):
#     with conn.cursor() as cur:
#         cur.execute(query)
#         return cur.fetchall()

# rows = run_query("SELECT * from mytable;")


# styles
day_header_style = '<p style="color:#7cbe5f; font-size: 40px;">'


# users
names = ["Murwan Eisa", "Cameron Toth"]
usernames = ["meisa", "ctoth"]
passwords = ['welcome123', 'hallo']

# encrypt passwords
hashed_passwords = stauth.Hasher(passwords).generate()


st.title("STRESS TRACKER")

authenticator = stauth.Authenticate(
    names,
    usernames,
    hashed_passwords,
    'some_cookie_name',
    'some_signature_key',
    cookie_expiry_days=30)


name, authentication_status, username = authenticator.login('Login', 'main')

weeklog = weekly_log.WeeklyLog()
moodlog = mood_log.MoodLog()

pages = [
    "Welcome",
    "Weekly activity",
    "Weekly mood",
    "Edit profile",
    "History"]

if authentication_status:
    with st.sidebar:
        webpage = st.radio('Navigation', pages)
        authenticator.logout('Logout', 'main')

    if webpage == "Welcome":
        st.write('Hello *%s*! Welcome back' % (st.session_state['name']))
        st.write(
            "Use the options in the sidepanel to fill in your weekplan or get insight into your performance.")

    elif webpage == "Weekly activity":
        weeklog.weeklog()
        if st.button('Confirm', key='log_ok'):
            weeklog.on_confirm()
            st.write("Weekly activity updated")

    elif webpage == "Weekly mood":
        moodlog.moodlog()
        if st.button('Confirm', key='mood_ok'):
            st.write("Weekly mood updated")

    elif webpage == "Edit profile":
        st.write("Modify your profile")

        edit_name = st.text_input('Name', st.session_state['name'])
        edit_username = st.text_input('Username', st.session_state['username'])
        edit_password = st.text_input('Password', "00000", type="password")

    elif webpage == "History":
        st.write("View your past logs")


elif authentication_status is False:
    st.error('Username/password is incorrect')
elif authentication_status is None:
    st.warning('Please enter your username and password')
