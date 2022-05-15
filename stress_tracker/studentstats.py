import streamlit as st
import altair as alt


class StudentStatistics:

    def __init__(self,db):
        self.db = db
        self.program = None
        self.degree = None

    def on_confirm(self):
        pass

    # student stats widget
    def showStats(self, program, degree):
        st.header("View student statistics")

        st.metric(label="Program", value=program)
        st.metric(label="Degree", value=degree)


        #retrieve course information
        q1 = "SELECT stats_year, stats_weeknr,user_id,stats_stress "
        q2 = "FROM user,stats "
        q3 = "WHERE (user.user_id = stats.stats_userid)"

        if (program != "All"):
            q3 += " AND user.user_program = '"+program+"'"
        if (degree != "All"):
            q3 += " AND user.user_degree = '"+degree+"'"

        query = q1 + q2 + q3
        result = self.db.customQuery(query)

        values = {"stress": [], "period": [], "user_id": []}
        for r in result:
            period = str(int(r[0]))+"-"+str(int(r[1]))
            values["period"].append(period)
            values["user_id"].append(r[2])
            values["stress"].append(r[3])

        students = set(values["user_id"])


        if len(students) == 0:
            st.write("Course program has no data yet.")
        else:
            weeks = set(values["period"])
            avg_stress = round(sum(values["stress"])/len(values["stress"]), 1)

            c1, c2, c3 = st.columns(3)
            c1.metric("Number of Students", len(students))
            c2.metric("Number of weeks monitored", len(weeks))
            c3.metric("Average stress level", avg_stress)

            # make stress chart
            week_dic = {w:[] for w in weeks}

            for i, v in enumerate(values["period"]):
                stress = values["stress"][i]
                week_dic[v].append(stress)

            values = []
            for w in week_dic:
                week_stress = sum(week_dic[w])/len(week_dic[w])
                values.append({'period': w, 'stress': week_stress,'avg_stress': avg_stress})

            data = alt.Data(values=values)
            chart_bar = alt.Chart(data).mark_bar().encode(
                x='period:O',
                y=alt.Y('stress:Q', scale=alt.Scale(domain=[1, 10]))
            )
            st.write("Weekly average stress levels.")
            st.write(chart_bar)

            st.write("Click on the activities below to see detailed statistics.")

            activities = ["sleep", "study", "work", "social", "hobby"]
            for a in activities:
                with st.expander(a.upper() + " STATS"):
                    # retrieve boundaries of activity
                    boundary = {}
                    for b in [0, 1]:
                        criterium = "(stats_degree='" + degree+"' AND stats_program='" + program + "' AND stats_bound =" + str(b)+")"
                        values = self.db.getColumnData("stats_"+a, "avg_stats", criterium)

                        if len(values) == 0:
                            criterium = "(stats_degree='Default' AND stats_program='Default' AND stats_bound ="+str(b)+")"
                            values = self.db.getColumnData("stats_"+a, "avg_stats", criterium)

                        boundary[b] = sum(values)/len(values)    

                    # make query
                    q1 = "SELECT stats_year,stats_weeknr,user_firstname,user_lastname,stats_stress,stats_"+a+" "
                    q2 = "FROM user,stats "
                    q3 = "WHERE (user.user_id = stats.stats_userid)"

                    if (program != "All"):
                        q3 += " AND user.user_program = '"+program+"'"
                    if (degree != "All"):
                        q3 += " AND user.user_degree = '"+degree+"'"

                    query = q1 + q2 + q3

                    # retrieve and transform student data
                    result = self.db.customQuery(query)
                    values = []

                    low_result = 0
                    high_result = 0

                    for r in result:
                        b = "normal"
                        if r[4] < boundary[0]:
                            b = "below"
                            low_result+=1
                        elif r[4] > boundary[1]:
                            b = "above"
                            high_result += 1

                        period = str(int(r[0]))+"-"+str(int(r[1]))
                        dic = {"period": period, "name": r[2]+" "+r[3], "hours": r[5], "stress": r[4], "boundary": b}
                        values.append(dic)

                    dom = ["normal", "below", "above"]
                    rng = ["white", "green", "red"]
                    data = alt.Data(values=values)
                    chart = alt.Chart(data).mark_circle().encode(
                        x='period:O',
                        y='hours:Q',
                        tooltip=['name:O', 'period:O', 'hours:Q', 'stress:Q'],
                        size='stress:Q',
                        color=alt.Color('boundary:O', scale=alt.Scale(domain=dom, range=rng))
                    )
                    st.subheader(a.upper())
                    st.write("Regular hours between " + str(int(boundary[0]))+"-" + str(int(boundary[1])))
                    st.write(chart)

                    p_low = int(round(100 * (low_result/len(result)), 0))
                    p_high = int(round(100 * (high_result/len(result)), 0))
                    col1, col2 = st.columns(2)
                    col1.metric("below boundary", str(p_low)+"%")
                    col2.metric("above boundary", str(p_high)+"%")
