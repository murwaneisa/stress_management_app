import streamlit as st
import joblib
from datetime import date


class Stress_ai:

    def __init__(self, userinfo, userstats):
        self.userdata = userinfo
        self.userstats = userstats

    def get_ai_stress_level(self, ai_data):
        model = joblib.load('stress_tracker/stress-tracker.joblib')
        predictions = model.predict([ai_data])
        return predictions[0]

    def ai_widget(self):
        # init variables
        # newdata: dictionary to store user data = db.userdata + db.userstats
        newdata = self.userdata.copy()
        newdata.update(self.userstats)

        # calculate age from DOB
        born = (newdata.get("user_dob"))[0]
        today = date.today()
        age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))

        # bunch of arrays
        gender = {"F": 1, "M": 2, "X": 3, "0": 4}
        # tags that are displayed for each input widget
        tags = ["Sleep", "Study", "Social activites", "Workout, sports", "Work", "Hobby",
                "Perceived stress level",
                "Migraines or Headaches", "Digestive issues", "Low energy, fatigue", "Relationship issues", "Financial troubles"]
        frequency = {
            0: "Prefer not to say",
            1: "Never",
            2: "Once or twice",
            3: "Sometimes",
            4: "Frequently",
            5: "All the time"
        }
        lst = ["user_gender", "stats_sleep", "stats_study", "stats_social", "stats_sport", "stats_work", "stats_hobby", "stats_stress", "stats_migraine", "stats_digest", "stats_energy", "stats_relation", "stats_financial"]

        ai_data = [age, ]

        for a in lst:
            ai_data.append(newdata.get(a)[0])
        ai_data[1] = gender.get(ai_data[1])

        # UI
        st.title("Stress Level Calculator AI")
        st.write("Try tweaking your values with the widgets below to see " +
                 "how changes to your routine might influence your stress levels.")
        ai_data[2] = st.slider(tags[0] + " (hours per day)", min_value=0, max_value=24, value=ai_data[2], format=None, help=None)

        # terrible design solution:
        i = 3
        for b, c in zip(ai_data[3:], tags[1:6]):
            ai_data[i] = st.slider(c, min_value=0, max_value=100, value=b, format=None, help=None)
            i += 1

        ai_data[i] = st.slider(tags[6], min_value=0, max_value=10, value=ai_data[8], format=None, help=None)
        i += 1

        for d, e in zip(ai_data[10:], tags[7:]):
            ai_data[i] = st.selectbox(e, frequency, index=d, format_func=lambda d: frequency.get(d))
            i += 1

        # st.write(ai_data)
        st.header("AI prediction: " + str(self.get_ai_stress_level(ai_data)))
        # st.write(self.get_ai_stress_level(19, 0, 8, 20, 15, 6, 40, 6, 2, 4, 4, 4, 4, 1))

# print(f'Your stress level is {get_ai_stress_level(19, 0, 8, 20, 15, 6, 40, 6, 2, 4, 4, 4, 4, 1)}')
# headache, digestion_problem, low_energy, relaxation, relationship, financial:-
# (0: 'Almost never', 1: 'Fairly often', 2: 'Never', 3: 'Sometimes', 4: 'Very often')
