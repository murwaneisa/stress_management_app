import streamlit as st

class MoodLog:
    def __init__(self):
        self.mood_slider = None

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

        self.mood_slider = st.select_slider(
            'How did you feel this week?', options=range(1, 11),
            format_func=lambda x: mood_options.get(x),
            )

    def add_comments(self):
        st.text_area("Additional comments", height=None, max_chars=None, key=None,
                     help="Write here anything that's happened this week that might've influenced your stress levels", on_change=None)
