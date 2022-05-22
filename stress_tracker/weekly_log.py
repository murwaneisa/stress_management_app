import streamlit as st
# import styles
# from datetime import datetime, timedelta


class WeeklyLog:

    def __init__(self, db, user_id,year,weeknr):
        self.db = db
        self.user_id = user_id
        self.year = year
        self.weeknr = weeknr

        self.activities = {'Study': 0, 'Work': 0, 'Social activities': 0, 'Workout, sports': 0, 'Hobbies': 0}
        self.other_issues = {}
        self.comments = ""

    # enter user input into database
    def on_confirm(self):
        values = {"stats_userid": [self.user_id, "int"],
                  "stats_year": [self.year, "int"],
                  "stats_weeknr": [self.weeknr, "int"]}

        name_dic = {'Study': "stats_study",
                    'Work': "stats_work",
                    'Social activities': "stats_social",
                    'Workout, sports': "stats_sport",
                    'Hobbies': 'stats_hobby'}

        for a in self.activities:
            value = self.activities[a]
            var_name = name_dic[a]
            values[var_name] = [value, "int"]

        # collect mood data
        for a in self.other_issues:
            var_name = "stats_"+a
            value = self.other_issues[a]
            values[var_name] = [value, "int"]

        # get comments
        values["stats_comments"] = [self.comments, "str"]

        # get_stress
        values["stats_stress"] = [self.mood_slider, "int"]

        # add new data to database
        self.db.insertData(values, "stats")

    def weeklog(self):
        st.header("Weekly activity & mood")

        c1, c2 = st.columns(2)
        c1.metric(label="Year", value=self.year)
        c2.metric(label="Weeknr", value=self.weeknr)
        st.write("")

        self.activitylog()

        st.write("")

        self.moodlog()
        self.add_comments()

        if st.button('Confirm'):
            self.on_confirm()
            st.write("Weekly activity updated")

    # weekly log widget
    def activitylog(self):

        st.subheader("Weekly activities")
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
        for a in self.activities:
            self.activities.update({a: (st.number_input(a, min_value=0, max_value=24, key=a,
                                                   help="Please provide total number of hours per week."))})

    def moodlog(self):
        mood_options = {
            1: "Extremely stressed",
            2: "Overwhelmingly stressed",
            3: "Very stressed",
            4: "Overall stressed",
            5: "A little stressed",
            6: "Fine",
            7: "Fairly relaxed",
            8: "Relaxed",
            9: "Carefree",
            10: "Excellent"
            }

        st.subheader("How did you feel this week?")
        self.mood_slider = st.select_slider("", options=range(1, 11), value=6,
            format_func=lambda x: mood_options.get(x))

        other_options = {
            "migraine": "Migraines or headaches",
            "digest": "Digestive issues",
            "insomnia": "Insomnia",
            "energy": "Low energy, fatigue",
            "financial": "Financial troubles",
            "relation": "Relationship issues",
        }

        frequency = {
            0: "Prefer not to say",
            1: "Never",
            2: "Once or twice",
            3: "Sometimes",
            4: "Frequently",
            5: "All the time"
        }

        st.subheader("How often did you experience the following:")
 
        for a in other_options:
            self.other_issues[a] = st.selectbox(other_options.get(a), frequency, index=1, format_func=lambda x: frequency.get(x), key=a)

    def add_comments(self):
        self.comments = st.text_area("Additional comments", height=None, max_chars=None, key=None,
                     help="Write here anything that's happened this week that might've influenced your stress levels",
                     on_change=None)
