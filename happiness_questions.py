import streamlit as st
import datetime
import os
import json

print_date = datetime.date.today()
# Create the form using Streamlit widgets
st.title(':green[**Happiness Questions**] 😄')
st.subheader(f':green[_{print_date}_]')
q1 = st.radio('Did I do my best to prioritize—but not pursue—happiness?', ('Yes', 'No'))
q2 = st.radio('Did I do my best to be self-compassionate (but not self-indulgent or self-pitying) when I failed at something??', ('Yes', 'No'))
q3 = st.radio('Did I do my best to be grateful for the good things that came my way?', ('Yes', 'No'))
q4 = st.radio('Did I do my best to pursue flow and steer myself towards doing something meaningful and engaging as opposed to seeking superiority?', ('Yes', 'No'))
q5 = st.radio('Did I do my best to not be a taker or matcher, but rather, a Giver?', ('Yes', 'No'))
q6 = st.radio('Did I do my best to practice kindness and generosity in “otherish” vs. “selfless” ways?', ('Yes', 'No'))
q7 = st.radio('Did I do my best to not be overly controlling of others or of outcomes??', ('Yes', 'No'))
q8 = st.radio('Did I do my best to take personal responsibility for my happiness (i.e., seek internal control)?', ('Yes', 'No'))
q9 = st.radio('Did I do my best to exercise “smart trust” (trust others more if low on trust)?', ('Yes', 'No'))
q10 = st.radio('Did I do my best to be forgiving of others?', ('Yes', 'No'))
q11 = st.radio('Did I do my best to look for positive consequences of even negative events?', ('Yes', 'No'))
q12 = st.radio('Did I do my best to practice mindfulness?', ('Yes', 'No'))

# When the form is submitted, save the answers
if st.button('Submit'):
    # Create json file if it does not exist
    if not os.path.isfile("happiness_scores.json"):
        with open("happiness_scores.json", "w") as f:
            empty_db = {
                'total': {},
                'daily': {}
            }
            json.dump(empty_db, f, indent=2)
    # Open the file for reading and load the dict to data
    with open("happiness_scores.json") as f:
        imported_data = json.load(f)
        daily_answers = imported_data['daily']
        total_answers = imported_data['total']

    today = str(datetime.datetime.today().strftime('%Y%m%d'))  # today's date
    # today = str(datetime.datetime.now())
    if today not in daily_answers:
        daily_answers[today] = {}

    answers = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12]  # add a list of the questions to variable
    st.success('Answers submitted ✅')  # prints if submission is successful

    question_num = 1
    for answer in answers:
        if str(question_num) not in total_answers:
            total_answers[str(question_num)] = {"Yes": 0, "No": 0}

        if answer == 'Yes':
            daily_answers[today][str(question_num)] = 1
            total_answers[str(question_num)]["Yes"] += 1
        elif answer == 'No':
            daily_answers[today][str(question_num)] = 0
            total_answers[str(question_num)]["No"] += 1
        question_num += 1

    filename = "happiness_scores.json"
    with open(filename, 'w') as f:
        json.dump({"total": total_answers, "daily": daily_answers}, f, indent=2)

# Calculate the score and display the graph
# store the data for each day somehow, in a dictionry
# the graph should have a line for total points
# Store what questions you frequently say no to
# maybe only include the total in he main dict to save data?
