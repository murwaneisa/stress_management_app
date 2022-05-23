import streamlit as st
import pandas as pd


class History:
    def __init__(self):
        pass

    def avg(self, values):
        total = sum(values)
        count = len(values)

        if total == 0:
            avg = 0
        else:
            avg = total/count

        return avg

    def page(self, user_stats):
        st.header("User history")
        st.subheader("Here you can see an overview of your statistics")

        st.write("These statistics are based on *%s* weeks." % str(len(user_stats["stats_id"])))
        st.write("y: hours per week,   x: week number")

        activities = {'sleep': "avg. per day",
                      'study': "hours a week",
                      'work': "hours a week",
                      'social': "hours a week",
                      'hobby': "hours a week"}

        for a in activities:
            values = user_stats["stats_"+a]
            print(values)
            label = a.upper() + " ("+activities[a]+")"

            if len(values) == 0:
                avg_v = "-"
                delta_v = "-"
            elif len(values) == 1:
                avg_v = round(self.avg(values), 1)
                delta_v = "-"
            elif len(values) > 1:
                avg_v = round(self.avg(values), 1)
                delta_v = round(avg_v - self.avg(values[0:-1]), 1)

            st.metric(label, avg_v, delta_v, delta_color="off")

            data = pd.DataFrame(data=values)
            st.line_chart(data=data, height=150)

        # Display a line chart of all comparable values
        st.subheader("A graph of all your past logs")
        lst = ["stats_study", "stats_work", "stats_social", "stats_sport", "stats_hobby"]
        all_weeks = {key: value for (key, value) in user_stats.items() if key in lst}
        chart_data = pd.DataFrame(data=all_weeks)
        st.line_chart(data=chart_data)
