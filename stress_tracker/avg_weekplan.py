import streamlit as st

class AvgWeekplan:

    def __init__(self,db,user_id):
        self.db = db
        self.user_id = user_id
        self.choice = [{},{}]

    def on_confirm(self, insert, program, degree):

        for b in [0,1]:
            values = {"stats_"+a:[self.choice[b][a],"int"] for a in self.choice[b]}
            
            if insert:
                values["stats_program"] = [program,"str"]
                values["stats_degree"] = [degree,"str"]
                values["stats_userid"] = [self.user_id,"int"]
                values["stats_bound"] = [b,"int"]

                self.db.insertData(values,"avg_stats")
            else:
                c1 = "stats_program ='"+program+"'" 
                c2 = "AND stats_degree='"+degree+"'"
                c3 = " AND stats_userid="+str(self.user_id)
                c4 = " AND stats_bound="+str(b)
                criteria = c1 + c2 + c3 + c4
                self.db.UpdateUserData(None,values,"avg_stats",criteria)


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
        print(avg_stats)

        indices = [i for i,v in enumerate(avg_stats["stats_program"]) if v == program]
        indices = [i for i in indices if avg_stats["stats_degree"][i] == degree]

        # use default data if it doesnt exist yet
        if len(indices)==0:
            indices = [i for i,v in enumerate(avg_stats["stats_program"]) if v == "Default"]
            indices = [i for i in indices if avg_stats["stats_degree"][i] == "Default"]
            new_profile = True
        else:
            new_profile = False

        print(indices)
        for a in activities:
            hours = [h for h in range(period[activities[a]][0],period[activities[a]][1]+1)]
            v_min = avg_stats["stats_"+a][indices[0]]
            v_max = avg_stats["stats_"+a][indices[1]]
            text = a.upper() + " ("+activities[a]+")"
            self.choice[0][a], self.choice[1][a] = st.select_slider(text, options=hours, value=(v_min,v_max))

        if st.button('Update'):
            p = program
            d = degree
            if p == "All":
                p = "Default"
            if d == "All":
                d = "Default"
            self.on_confirm(new_profile,p,d)
            st.write("Average weekplan updated.")
