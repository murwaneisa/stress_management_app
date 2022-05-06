# full credit to M Khorasani for streamlit_authenticator

import streamlit as st
import streamlit_authenticator as stauth
import weekly_log, mood_log, signup, connector, history

# page config
st.set_page_config(
     page_title="Stress Tracker",
     page_icon="🐛",
     layout="centered",
     initial_sidebar_state="expanded",
     menu_items={
         'Get Help': 'https://www.github.com/',
         'Report a bug': "https://www.github.com/",
         'About': ""
     }
 )

# session state
if 'hour_counter' not in st.session_state:
    st.session_state['hour_counter'] = 0
# st.session_state['date_counter'] = []


# users
names = ["Murwan Eisa", "Cameron Tóth", "Test User"]
usernames = ["meisa", "ctoth", "test"]
passwords = ['welcome123', 'hallo', 'test']

# encrypt passwords
hashed_passwords = stauth.Hasher(passwords).generate()

authenticator = stauth.Authenticate(
    names,
    usernames,
    hashed_passwords,
    'some_cookie_name',
    'some_signature_key',
    cookie_expiry_days=30)

# login widget
name, authentication_status, username = authenticator.login('Login', 'main')

# init objects
weeklog = weekly_log.WeeklyLog()
moodlog = mood_log.MoodLog()
connector = connector.Database()
signup = signup.Signup(connector)
history = history.History()

# sidebar menu options
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
        st.header('Hello *%s*! Welcome back' % (st.session_state['name']))
        st.write(
            "Use the options in the sidepanel to fill in your weekplan or get insight into your performance.")

    elif webpage == "Weekly activity":
        weeklog.weeklog()

    elif webpage == "Weekly mood":
        moodlog.moodlog()
        moodlog.add_comments()
        if st.button('Submit', key='mood_ok'):
            st.write("Weekly mood updated")


    elif webpage == "Edit profile":
        st.write("Modify your profile")

        edit_name = st.text_input('Name', st.session_state['name'])
        edit_username = st.text_input('Username', st.session_state['username'])
        edit_password = st.text_input('Password', "00000", type="password")

    elif webpage == "History":
        history.page()


elif authentication_status is False:
    st.error('Username/password is incorrect')

elif authentication_status is None:
    st.warning('Please enter your username and password, or sign up below!')
    if st.button("Sign up"):
        st.header("Sign up")
        signup.signup()
        newemail, newpsw = signup.on_confirm()
