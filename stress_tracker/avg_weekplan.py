import streamlit as st

class AvgWeekplan:

    def __init__(self,db,user_id):
        self.db = db
        self.user_id = user_id
        self.choice_min = {}
        self.choice_max = {}

    def on_confirm(self):
        pass

    # weekly log widget
    def weekplan(self, program, degree):
        period = {"avg. per day": [0,20], "hours a week": [0,60]}
        activities = {'sleep': "avg. per day",
                      'study': "hours a week",
                      'work': "hours a week",
                      'social': "hours a week",
                      'hobby': "hours a week"}

        st.header("Average student profile")
        st.metric(label="Program", value=program)
        st.metric(label="Degree", value=degree)

        st.write("")
        st.write("Use the options below to specify an ideal student weekplan.")
        st.write("Use the sliders to define the minimum and maximum suggested hours of an activity.")

        # retrieve existing data
        avg_stats = self.db.getUserData("avg_stats", self.user_id)

        indices = [i for i,v in enumerate(avg_stats["stats_program"]) if v == program]
        indices = [i for i in indices if avg_stats["stats_degree"][i] == degree]

        # use default data if it doesnt exist yet
        if len(indices)==0:
            indices = [i for i,v in enumerate(avg_stats["stats_program"]) if v == "Default"]
            indices = [i for i in indices if avg_stats["stats_degree"][i] == "Default"]

        for a in activities:
            hours = [h for h in range(period[activities[a]][0],period[activities[a]][1]+1)]
            v_min = avg_stats["stats_"+a][indices[0]]
            v_max = avg_stats["stats_"+a][indices[1]]
            text = a.upper() + " ("+activities[a]+")"
            self.choice_min[a], self.choice_max[a] = st.select_slider(text, options=hours, value=(v_min,v_max))

        if st.button('Update'):
            self.on_confirm()
            st.write("Average weekplan updated.")
