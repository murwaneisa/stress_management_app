import streamlit as st
# import styles
from datetime import datetime, timedelta


class WeeklyLog:

    def __init__(self):
        self.period_checkboxes = {}
        self.hour_checkboxes = {}
        self.date = None

    def on_confirm(self):
        pass

    # weekly log widget
    def weeklog(self):
        if 'hour_counter' not in st.session_state:
            st.session_state['hour_counter'] = 0
            # st.session_state['date_counter'] = []

        activities = ['Sleep', 'Study', 'Work', 'Social', 'Hobby']

        st.header("Weekly log")

        # today = datetime.now()
        # n_days_ago = today - timedelta(days=7)
        # st.subheader("Enter which date your submission applies for:")
        # self.date = st.date_input("Date", value=None, min_value=n_days_ago, max_value=today, key=None)

        st.subheader("On avarage, how many hours did you dedicate to the following every day this week?")
        st.write("You are expected to provide an estimated daily avarage to the best of your abilities.")
        hours = []
        for a in activities:
            hours.append(st.number_input(a, min_value=0, max_value=24, key=a, on_change=None))
        st.session_state['hour_counter'] = sum(hours)
        st.write(f"Total amount of hours accounted for: {st.session_state['hour_counter']}")
        if st.session_state['hour_counter'] <= 24:
            if st.button('Confirm'):
                self.on_confirm()
                st.write("Weekly activity updated")
        else:
            st.write(f"There are less than {st.session_state['hour_counter']} hours in a day!")
