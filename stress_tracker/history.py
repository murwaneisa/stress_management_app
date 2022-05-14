import streamlit as st


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

    def page(self,user_stats):
        st.header("View your historical data")
        st.subheader("Here you can view your average weekly statistics")

        st.write("These statistics are based on *%s* weeks." % str(len(user_stats["stats_id"])))

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

            st.metric(label, avg_v, delta_v, "inverse")
