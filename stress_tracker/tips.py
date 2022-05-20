import streamlit as st


class Tips:

    def __init__(self,db):
        self.db = db
        self.program = None
        self.degree = None

    # student stats widget
    def showTips(self, user_info, user_stats):
        st.header("Tips")

        print(user_info)
        program = user_info["user_program"][0]
        degree = user_info["user_degree"][0]

        if len(user_stats["stats_id"]) == 0:
            st.write("We have not received any data from you yet.")

        else:
            # retrieve existing data
            activities = ["sleep", "study", "work", "social", "hobby"]

            for p in ["avg", "last_week"]:

                if p == "avg":
                    st.subheader("Relevant tips based on your average statistics.")
                elif p == "last_week":
                    st.subheader("Relevant tips based on your recent statistics.")

                for a in activities:
                    boundary = {}
                    for b in [0, 1]:
                        criterium = "(stats_degree='"+degree+"' AND stats_program='"+program+"' AND stats_bound ="+str(b)+")"
                        values = self.db.getColumnData("stats_"+a, "avg_stats", criterium)

                        if len(values) == 0:
                            criterium = "(stats_degree='Default' AND stats_program='Default' AND stats_bound ="+str(b)+")"
                            values = self.db.getColumnData("stats_"+a, "avg_stats", criterium)

                        boundary[b] = sum(values)/len(values)

                    v = user_stats["stats_"+a]

                    if p == "avg":
                        avg = sum(v)/len(v)

                        if avg > boundary[1]:
                            st.write("- It looks like your average "+a+" hours are quite high. Maybe you can lower it a bit.")
                        elif avg < boundary[0]:
                            st.write("- It looks like your average "+a+" hours are low. Maybe you can increase it a bit.")
                        else:
                            st.write("- Your "+a+" habits look great. Nice job!")

                    elif p == "last_week":
                        avg = v[-1]

                        if avg > boundary[1]:
                            st.write("- You did "+a+" a lot last week. Maybe you can lower it a bit.")
                        elif avg < boundary[0]:
                            st.write("- Your "+a+" hours were low last week. Maybe you can increase it a bit.")
                        else:
                            st.write("- Last weeks "+a+" hours were good. Keep it up!")

