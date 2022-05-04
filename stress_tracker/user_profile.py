import streamlit as st


def user_profile():
    def calcHours(period, ckey):

        total = 0

        for k in hour_checkbox:
            if not hour_checkbox[k]:
                total += 1

    day_header_style = '<p style="color:Green; font-size: 20px;">'

    pages = ["Welcome", "Weekly activity", "Weekly mood", "Edit profile", "Histor"]
    webpage = st.radio("Navigation", pages)

    if webpage == "Welcome":
        st.write("Hello *%s*! Welcome back")
        st.write(
            "Use the options in the sidepanel to fill in your weekplan or get insight into your performance."
        )

    elif webpage == "Weekly activity":
        options = st.multiselect(
            "What did you do this week?", ["Study", "Work", "Socialize", "Hobby"]
        )

        if "Study" in options:
            st.write("STUDY TIME")
            days = [
                "Monday",
                "Tuesday",
                "Wednesday",
                "Thursday",
                "Friday",
                "Saturday",
                "Sunday",
            ]
            periods = {
                "00:00-05:00": [0, 1, 2, 3, 4],
                "05:00-09:00": [5, 6, 7, 8],
                "09:00-17:00": [9, 10, 11, 12, 13, 14, 15, 16],
                "17:00-00:00": [17, 18, 19, 20, 21, 22, 23],
            }

            period_checkbox = {}
            hour_checkbox = {}
            cols = st.columns(len(days))

            for i, day in enumerate(days):
                header = day_header_style + days[i] + "</p>"
                cols[i].markdown(header, unsafe_allow_html=True)

                for period in periods:
                    period_str = str(i) + "_" + period
                    period_checkbox[period_str] = cols[i].checkbox(
                        label=period, key=period_str
                    )

                    with cols[i].expander("hours"):
                        for h in periods[period]:
                            time_str = "{:02}:00-{:02}:00".format(h, h + 1)
                            key_str = str(i) + "_" + str(h)
                            hour_checkbox[key_str] = st.checkbox(
                                label=time_str,
                                key=key_str,
                                value=period_checkbox[period_str],
                            )

        if st.button("Confirm"):
            st.write("Weekly activity updated")

    elif webpage == "Weekly mood":
        mood_slider = st.select_slider(
            "How did you feel this week?",
            options=[
                "Super Stressed",
                "Restless",
                "Stressed",
                "Okay",
                "Fine",
                "Great",
                "Amazing",
            ],
        )

        if st.button("Confirm"):
            st.write("Weekly mood updated")

    elif webpage == "Edit profile":
        st.write("modify your profile")

        edit_name = st.text_input("Name", st.session_state["name"])
        edit_username = st.text_input("Username", st.session_state["username"])
        edit_password = st.text_input("Password", "00000", type="password")

    elif webpage == "History":
        st.write("view your past performance")
