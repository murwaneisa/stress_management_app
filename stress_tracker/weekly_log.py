import streamlit as st
# import styles
# from datetime import datetime, timedelta


class WeeklyLog:

    def __init__(self, db, user_id):
        self.db = db
        self.user_id = user_id

    # enter user input into database
    def on_confirm(self, values):
        pass

    # weekly log widget
    def weeklog(self):

        st.header("Weekly log")
        st.subheader("On avarage, how many hours did you dedicate to the following activities this week?")

        # sleep: hours/day
        st.markdown("You are expected to provide an estimated *daily* avarage to the best of your abilities.")
        sleep_hours = st.slider("Sleep", min_value=0, max_value=24, value=8, step=None, format="%d hours",
                                help="Please provide avarage number of hours per day.")
        if sleep_hours >= 15:
            st.write("Are you sure you slept *%s* hours a day?" % str(sleep_hours))
            st.button("Get help")

        # activities: hours/week
        st.write("")
        st.markdown("You are expected to provide an estimated *total* number of hours.")
        activities = {'Study': 0, 'Work': 0, 'Social activities': 0, 'Workout, sports': 0, 'Hobbies': 0}
        for a in activities:
            activities.update({a: (st.number_input(a, min_value=0, max_value=24, key=a,
                                                   help="Please provide total number of hours per week."))})
        if st.button('Confirm'):
            self.on_confirm(activities)
            st.write("Weekly activity updated")
