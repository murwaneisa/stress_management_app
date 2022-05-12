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

        st.title("How did you feel this week?")
        self.mood_slider = st.select_slider("", options=range(1, 11),
            format_func=lambda x: mood_options.get(x))

        other_options = {
            "migraine": "Migraines",
            "digestive": "Digestive issues",
            "insomnia": "Insomnia",
            "energy": "Low energy, fatigue",
            "financial": "Financial troubles",
            "relationship": "Relationship issues",
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
        other_issues = []
        for a in other_options:
            other_issues.append(st.selectbox(other_options.get(a), frequency, index=1, format_func=lambda x: frequency.get(x), key=a))
        #     if st.checkbox(other_options.get(a), value=False, key=a, on_change=None):
        #         other_issues.append(a)
        # st.write("The following issues are going to be registered: ")
        # for i in other_issues:
        #     st.write(i)
        #     st.write(other_options.get(i))

    def add_comments(self):
        st.text_area("Additional comments", height=None, max_chars=None, key=None,
                     help="Write here anything that's happened this week that might've influenced your stress levels",
                     on_change=None)
