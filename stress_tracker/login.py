# full credit to M Khorasani for streamlit_authenticator
import datetime as dt
import streamlit as st
import streamlit_authenticator as stauth
import weekly_log, mood_log, signup, connector, history
import global_vars




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


# init objects
weeklog = weekly_log.WeeklyLog()
moodlog = mood_log.MoodLog()
db = connector.Database("test_config.ini")
signup = signup.Signup(db)
history = history.History()


#make database connection
db.connect_database()

usernames = db.getColumnData("user_username","user")
passwords = db.getColumnData("user_password","user")
userids = db.getColumnData("user_id","user")

# encrypt passwords
hashed_passwords = stauth.Hasher(passwords).generate()

authenticator = stauth.Authenticate(
    userids,
    usernames,
    hashed_passwords,
    'some_cookie_name',
    'some_signature_key',
    cookie_expiry_days=30)

# login widget
name, authentication_status, username = authenticator.login('Login', 'main')



# sidebar menu options


if authentication_status:
    user_id = st.session_state['name']
    user_info = db.getUserData(user_id,"user")
    user_stats = db.getUserData(user_id,"stats")

    #get current year and last weeknr
    current_date = dt.date.today() 
    weeknr = current_date.isocalendar()[1] -1
    year = current_date.isocalendar()[0]

    if weeknr == 0:
        year -= 1
        date = dt.date(year, 12, 31)
        weeknr = date.isocalendar()[1]

    lastrec_year = user_stats['stats_year'][-1]
    lastrec_weeknr = user_stats['stats_weeknr'][-1]

    if (year == lastrec_year) and (weeknr == lastrec_weeknr):
        give_feedback = False
        pages = ["Welcome",
                 "Edit profile",
                 "History"]
    else:
        give_feedback = True
        pages = ["Welcome",
                 "Weekly activity",
                 "Weekly mood",
                 "Edit profile",
                 "History"]

    with st.sidebar:
        webpage = st.radio('Navigation', pages)
        authenticator.logout('Logout', 'main')

    if webpage == "Welcome":
        st.header('Hello *%s*! Welcome back' % (user_info["user_firstname"][0]))

        if give_feedback:
            st.write("You can still give feedback of last week.")
            st.write(
                "Use the sidepanel options to fill in your weekplan or get insight into your performance.")
        else:
            st.write("You already gave last weeks feedback.")
            st.write("Use the side panel options to get insight into your performance.")

    elif webpage == "Weekly activity":
        weeklog.weeklog()

    elif webpage == "Weekly mood":
        moodlog.moodlog()
        moodlog.add_comments()
        if st.button('Submit', key='mood_ok'):
            st.write("Weekly mood updated")


    elif webpage == "Edit profile":
        #retrieve user data
        user_info = db.getUserData(user_id,"user")

        st.write("Modify your profile details")

        #text of variables and input options
        stat_description = {"user_username":["Username","str"],
                            "user_password":["Password","str"],
                            "user_firstname":["First name","str"],
                            "user_lastname":["Last name","str"],
                            "user_gender":["Gender",global_vars.gender_options],
                            "user_email":["E-mail","str"],
                            "user_program":["Course program",global_vars.course_options],
                            "user_degree":["Degree type",global_vars.degree_options],
                            "user_dob":["Date of Birth","date"],
                            "user_studystart":["First year of study","int"]}

        #generate input boxes
        input = {}
        for stat in stat_description.keys():
            text,input_option = stat_description[stat]
            org_value = user_info[stat][0]

            if type(input_option) is list:
                input[stat] = st.selectbox(text, input_option,index=input_option.index(org_value))
            elif input_option == "date":
                input[stat] = st.date_input(text, value=org_value, min_value=dt.datetime(1900, 1, 1))
            elif input_option == "str":
                if stat == "user_password":
                    input[stat] = st.text_input(text, max_chars=70, value=org_value, type="password")
                else:
                    input[stat] = st.text_input(text, max_chars=70, value=org_value)
            elif input_option == "int":
                input[stat] = st.number_input(text, min_value=1900, max_value=None, value=org_value, step=None, format=None)

        #confirm changes
        if st.button('Confirm'):
            values = {}
            for stat in input:

                org_value = user_info[stat][0]
                new_value = input[stat]

                if org_value != new_value:
                    if stat_description[stat][1] == "int":
                        datatype = "int"
                    else: 
                        datatype = "str"

                    values[stat] = [new_value,datatype]
            
            #update database 
            db.UpdateUserData(user_id,values,"user")
            st.write("Profile details updated")

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
