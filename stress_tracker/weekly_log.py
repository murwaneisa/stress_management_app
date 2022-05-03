import streamlit as st
import login


class WeeklyLog:

    def __init__(self):
        self.period_checkbox = {}
        self.hour_checkbox = {}
        self.option = None

    def calcHours(self, period, ckey):
        total = 0
        for k in self.hour_checkbox:
            if not self.hour_checkbox[k]:
                total += 1

    # weekly log widget
    def weeklog(self):
        self.option = st.selectbox(
                    "What did you do this week?", [
                        'Study', 'Work', 'Socialize', 'Hobby', 'Sleep'])

    #if "Study" in options:
        st.write("%s TIME" % (self.option).upper())
        days = [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday"]

        periods = {"00:00-05:00": [0, 1, 2, 3, 4],
                "05:00-09:00": [5, 6, 7, 8],
                "09:00-17:00": [9, 10, 11, 12, 13, 14, 15, 16],
                "17:00-00:00": [17, 18, 19, 20, 21, 22, 23]}

        cols = st.columns(len(days))

        for i, day in enumerate(days):
            header = login.day_header_style + days[i] + "</p>"
            cols[i].markdown(header, unsafe_allow_html=True)

            for period in periods:
                period_str = str(i) + "_" + period
                self.period_checkbox[period_str] = cols[i].checkbox(
                    label=period, key=period_str)

                with cols[i].expander("hours"):
                    for h in periods[period]:
                        time_str = '{:02}:00-{:02}:00'.format(h, h + 1)
                        key_str = str(i) + "_" + str(h)
                        self.hour_checkbox[key_str] = st.checkbox(
                            label=time_str, key=key_str, value=self.period_checkbox[period_str])
