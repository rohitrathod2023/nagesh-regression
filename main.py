import streamlit as st
import pickle
import numpy as np

# Load the saved model
with open('titanic_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Add an image of the Titanic ship at the top
#st.image('titanic_ship.png', caption="The Titanic", use_column_width=True)

st.title("Would you survive the Titanic disaster?")

# User inputs for the prediction
pclass = st.selectbox("What passenger class are you?", ("FirstClass", "SecondClass", "ThirdClass"))
gender = st.selectbox("What is your gender?", ("Male", "Female"))
age = st.slider("How old are you?", 1, 80, 25)  # min age: 1, max age: 80, default: 25
sibsp = st.slider("How many siblings and spouses were with you?", 0, 8, 1)  # 0 to 8 siblings/spouses
parch = st.slider("How many parents and children were aboard with you?", 0, 6, 0)  # 0 to 6 parents/children
fare = st.slider("How much did you pay for your cruise ticket? (in 1910 USD)", 0, 512, 92)  # Ticket price slider
embarked = st.selectbox("Which port did you embark from?", ("Cherbourg", "Queenstown", "Southampton"))

# Convert inputs to numerical values for the model
pclass_map = {"FirstClass": 1, "SecondClass": 2, "ThirdClass": 3}
gender_map = {"Male": 1, "Female": 0}
embarked_map = {"Cherbourg": 0, "Queenstown": 1, "Southampton": 2}

# Prepare input array for the model
user_input = np.array([[
    pclass_map[pclass],
    gender_map[gender],
    age,
    sibsp,
    parch,
    fare,
    embarked_map[embarked]
]])

# Button for prediction
if st.button('Submit'):
    prediction = model.predict(user_input)

    if prediction == 1:
        st.success("You would have survived the Titanic disaster!")
    else:
        st.error("Unfortunately, you would not have survived.")
