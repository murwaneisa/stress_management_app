import joblib

class Stess_ai:

    def get_ai_stress_level(age, gender, sleep, study, socialize, activity, work, hobby, headache, digestion_problem, low_energy, relaxation, relationship, financial):
        model = joblib.load('/Users/ahmedmohammed/Desktop/stress_tracker/stress_tracker_app/stress_tracker/stress-tracker.joblib')
        predictions = model.predict([ [age, gender, sleep, study, socialize, activity, work, hobby, headache, digestion_problem, low_energy, relaxation, relationship, financial] ])
        return predictions[0]

    print(f'Your stress level is {get_ai_stress_level(19, 0, 8, 20, 15, 6, 40, 6, 2, 4, 4, 4, 4, 1)}')


# Gender (0: Female, 1: Male, 2: Other, 3: Prefer not to say)
# headache, digestion_problem, low_energy, relaxation, relationship, financial:-
# (0: 'Almost never', 1: 'Fairly often', 2: 'Never', 3: 'Sometimes', 4: 'Very often')