# full credit to M Khorasani for streamlit_authenticator
import datetime as dt
import streamlit as st
import streamlit_authenticator as stauth
import weekly_log, mood_log, signup, connector, history, avg_weekplan, studentstats
import tips
import global_vars
import stress_ai


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


@st.cache(allow_output_mutation=True)
def get_data():
    return []


# init objects
db = connector.Database("test_config.ini")
signup = signup.Signup(db)

# make database connection
db.connect_database()

usernames = db.getColumnData("user_username", "user")
userpasswords = db.getColumnData("user_password", "user")
userids = db.getColumnData("user_id", "user")

# admin data
adminnames = db.getColumnData("admin_username", "admin")
adminpasswords = db.getColumnData("admin_password", "admin")
adminids = db.getColumnData("admin_id", "admin")

passwords = userpasswords + adminpasswords
login_names = usernames + adminnames
login_ids = userids + adminids


# encrypt passwords
# hashed_passwords = stauth.Hasher(passwords).generate()
# st.write(hashed_passwords)

# authenticator
authenticator = stauth.Authenticate(
    login_ids,
    login_names,
    passwords,
    'some_cookie_name',
    'some_signature_key',
    cookie_expiry_days=30)

# login widget
name, authentication_status, username = authenticator.login('Login', 'main')

# sidebar menu options
if authentication_status:
    user_id = st.session_state['name']

    user_name = st.session_state['username']
    user_type = "user"
    if user_name in adminnames:
        user_type = "admin"

    print(user_type)
    user_info = db.getUserData(user_type, user_id)

    # student user
    if user_type == "user":
        user_stats = db.getUserData("stats", user_id)
        user_info = db.getUserData("user", user_id)

        # get current year and last weeknr
        current_date = dt.date.today()
        weeknr = current_date.isocalendar()[1] - 1
        year = current_date.isocalendar()[0]
        if weeknr == 0:
            year -= 1
            date = dt.date(year, 12, 31)
            weeknr = date.isocalendar()[1]

        # check if user has stats
        if len(user_stats["stats_id"]) > 0:
            lastrec_year = user_stats['stats_year'][-1]
            lastrec_weeknr = user_stats['stats_weeknr'][-1]

            if (year == lastrec_year) and (weeknr == lastrec_weeknr):
                give_feedback = False
            else:
                give_feedback = True
        else:
            give_feedback = True

        # init classes
        weeklog = weekly_log.WeeklyLog(db, user_id, year, weeknr)
        moodlog = mood_log.MoodLog()
        tips = tips.Tips(db)
        history = history.History()

        # check if user has given feedback this week
        if give_feedback:
            pages = ["Welcome",
                     "Weekly activity & mood",
                     "History",
                     "Tips",
                     "Stress AI",
                     "Edit profile"]
        else:
            pages = ["Welcome",
                     "History",
                     "Tips",
                     "Stress AI",
                     "Edit profile"]

    # admin user
    elif user_type == "admin":
        avgWeekplan = avg_weekplan.AvgWeekplan(db, user_id)
        studentStats = studentstats.StudentStatistics(db)

        if len(get_data()) > 0:
            active_program, active_degree = get_data()[-1]
        else:
            active_program, active_degree = "All", "All"

        pages = ["Welcome",
                 "Avg. weekplan",
                 "Student statistics",
                 "Edit profile"]

    with st.sidebar:
        webpage = st.radio('Navigation', pages)
        authenticator.logout('Logout', 'main')

    # student/admin pages
    if webpage == "Welcome":
        if user_type == "user":
            st.header('Hello *%s*! Welcome back' % (user_info["user_firstname"][0]))
            if give_feedback:
                st.write("You can still give feedback of last week.")
                st.write(
                    "Use the sidepanel options to fill in your weekplan or get insight into your performance.")
            else:
                st.write("You already gave feedback of last week.")
                st.write("Use the side panel options to get insight into your performance.")
        elif user_type == "admin":
            st.header('Hello *%s*.' % (user_info["admin_firstname"][0]))
            st.subheader("Select the relevant program and degree.")

            course_options = ["All"]+list(global_vars.course_options)
            degree_options = ["All"]+list(global_vars.degree_options)

            program = st.selectbox("Program", course_options, index=course_options.index(active_program))
            degree = st.selectbox("Degree", degree_options, index=degree_options.index(active_degree))

            if st.button("Confirm"):
                get_data().append([program, degree])
                print(get_data())

            st.write("Use the sidepanel options to evaluate student performance of this track.")

    elif webpage == "Edit profile":
        # retrieve user data

        st.write("Modify your profile details")

        # text of variables and input options
        if user_type == "user":
            stat_description = {"user_username": ["Username", "str"],
                                "user_password": ["Password", "str"],
                                "user_firstname": ["First name", "str"],
                                "user_lastname": ["Last name", "str"],
                                "user_gender": ["Gender", global_vars.gender_options],
                                "user_email": ["E-mail", "str"],
                                "user_program": ["Course program", global_vars.course_options],
                                "user_degree": ["Degree type", global_vars.degree_options],
                                "user_dob": ["Date of Birth", "date"],
                                "user_studystart": ["First year of study", "int"]}

        elif user_type == "admin":
            stat_description = {"admin_username": ["Username", "str"],
                                "admin_password": ["Password", "str"],
                                "admin_firstname": ["First name", "str"],
                                "admin_lastname": ["Last name", "str"],
                                "admin_email": ["E-mail", "str"]}

        # generate input boxes
        input = {}
        for stat in stat_description.keys():
            text, input_option = stat_description[stat]
            org_value = user_info[stat][0]

            if type(input_option) is list:
                input[stat] = st.selectbox(text, input_option, index=input_option.index(org_value))
            elif input_option == "date":
                input[stat] = st.date_input(text, value=org_value, min_value=dt.datetime(1900, 1, 1))
            elif input_option == "str":
                if "password" in stat:
                    input[stat] = st.text_input(text, max_chars=70, value=org_value, type="password")
                else:
                    input[stat] = st.text_input(text, max_chars=70, value=org_value)
            elif input_option == "int":
                input[stat] = st.number_input(text, min_value=1900, max_value=None, value=org_value)

        # confirm changes
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

                    values[stat] = [new_value, datatype]

            # update database
            db.UpdateUserData(user_id, values, user_type)

            st.write("Profile details updated")

    # user pages
    elif webpage == "Weekly activity & mood":
        weeklog.weeklog()

    elif webpage == "Weekly mood":
        moodlog.moodlog()
        moodlog.add_comments()
        if st.button('Submit', key='mood_ok'):
            st.write("Weekly mood updated")

    elif webpage == "History":
        user_stats = db.getUserData("stats", user_id)
        history.page(user_stats)

    elif webpage == "Tips":
        user_info = db.getUserData("user", user_id)
        user_stats = db.getUserData("stats", user_id)

        tips.showTips(user_info, user_stats)

    elif webpage == "Stress AI":
        user_stats = db.getUserData("stats", user_id)
        stress_ai = stress_ai.Stress_ai(user_info, user_stats)
        stress_ai.ai_widget()

    # admin pages
    elif webpage == "Avg. weekplan":

        print(active_program, active_degree)
        avgWeekplan.weekplan(active_program, active_degree)

    elif webpage == "Student statistics":
        studentStats.showStats(active_program, active_degree)

elif authentication_status is False:
    st.error('Username/password is incorrect')

elif authentication_status is None:
    st.warning('Please enter your username and password, or sign up below!')
    signup_button = st.button("Sign up")
    if 'signup_active' not in st.session_state:
        st.session_state['signup_active'] = False
    if signup_button:
        st.session_state['signup_active'] = True
    if st.session_state['signup_active']:
        st.header("Sign up")
        signup.signup()
        # newuser, newpsw =
        signup.on_confirm()
