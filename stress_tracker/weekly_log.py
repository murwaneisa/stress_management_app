import streamlit as st
# import styles
from datetime import datetime, timedelta


class WeeklyLog:

    def __init__(self):
        self.period_checkboxes = {}
        self.hour_checkboxes = {}
        # self.activity = None
        self.date = None
        # self.days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        # self.periods = {"00:00-05:00": [0, 1, 2, 3, 4],
        #         "05:00-09:00": [5, 6, 7, 8],
        #         "09:00-17:00": [9, 10, 11, 12, 13, 14, 15, 16],
        #         "17:00-00:00": [17, 18, 19, 20, 21, 22, 23]}
        # self.cols = None
        # self.used_keys = []

    # def calcHours(self, period, ckey):
    #     total = 0
    #     for k in self.hour_checkboxes:
    #         if not self.hour_checkboxes[k]:
    #             total += 1

    # weekly log widget
    def weeklog(self):
        if 'hour_counter' not in st.session_state:
            st.session_state['hour_counter'] = 0
            st.session_state['date_counter'] = []

        activities = ['Sleep', 'Study', 'Work', 'Social', 'Hobby']

        st.header("Weekly log")

        today = datetime.now()
        n_days_ago = today - timedelta(days=7)
        st.subheader("Enter which date your submission applies for:")
        self.date = st.date_input("Date", value=None, min_value=n_days_ago, max_value=today, key=None)

        st.subheader("How many hours did you dedicate to the following?")
        hours = []
        for a in activities:
            hours.append(st.number_input(a, min_value=0, max_value=24, key=a, on_change=None))
        st.session_state['hour_counter'] = sum(hours)
        st.write("Total amount of hours accounted for: ", st.session_state['hour_counter'])

    def on_confirm(self):
        pass
