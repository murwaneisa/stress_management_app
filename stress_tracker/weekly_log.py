import streamlit as st
import styles


class WeeklyLog:

    def __init__(self):
        self.period_checkboxes = {}
        self.hour_checkboxes = {}
        self.activity = None
        self.days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        self.periods = {"00:00-05:00": [0, 1, 2, 3, 4],
                "05:00-09:00": [5, 6, 7, 8],
                "09:00-17:00": [9, 10, 11, 12, 13, 14, 15, 16],
                "17:00-00:00": [17, 18, 19, 20, 21, 22, 23]}
        self.cols = None
        self.used_keys = []

    def calcHours(self, period, ckey):
        total = 0
        for k in self.hour_checkboxes:
            if not self.hour_checkboxes[k]:
                total += 1

    # weekly log widget
    def weeklog(self):
        self.activity = st.selectbox(
                    "What did you do this week?", [
                        'Study', 'Work', 'Social', 'Hobby', 'Sleep'])
        
        if self.used_keys not in st.session_state:
            st.session_state.used_keys = []

    # if "Study" in options:
        st.write("%s TIME" % (self.activity).upper())
        self.cols = st.columns(len(self.days))
        for i, day in enumerate(self.days):
            # i = day
            # styles
            header = styles.day_header_style + self.days[i] + "</p>"
            self.cols[i].markdown(header, unsafe_allow_html=True)

            for period in self.periods:
                period_str = str(i) + "_" + period
                self.period_checkboxes[period_str] = self.cols[i].checkbox(
                    label=period, key=period_str)

                with self.cols[i].expander("hours"):
                    for h in self.periods[period]:
                        time_str = '{:02}:00-{:02}:00'.format(h, h + 1)
                        key_str = str(i) + "_" + str(h)
                        if key_str not in self.used_keys:                            
                            self.hour_checkboxes[key_str] = st.checkbox(label=time_str,
                                                                        key=key_str, value=self.period_checkboxes[period_str])


    def on_confirm(self):
        # for saving user input on confirm
        for i, day in enumerate(self.days):
            for period in self.periods:
                for h in self.periods[period]:
                    key_str = str(i) + "_" + str(h)
                    #st.write(key_str)
                    st.write(st.session_state[key_str])
                    if self.hour_checkboxes[key_str]:
                        if not st.session_state[key_str]:
                            # INSERT i = day, h = 1 hour
                            st.write("INSERT")
                            pass
                        else:
                            st.write("HEWWO")
                        self.used_keys.append(key_str)
                        # st.write(st.session_state['key_str'])
                        # st.write(self.hour_checkboxes[key_str])
        st.write(self.used_keys)
