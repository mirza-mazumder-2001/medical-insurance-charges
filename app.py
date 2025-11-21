import streamlit as st
import pandas as pd
import pickle

model = pickle.load(open("model.sav", "rb"))

st.title("💰 Insurance Charge Prediction")
st.write("Enter the details to predict the insurance charge.")

age = st.number_input("Age", min_value=18, max_value=100, value=30)
bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, value=25.0)
children = st.number_input("Number of Children", min_value=0, max_value=10, value=0)
smoker = st.selectbox("Smoking?", ["No", "Yes"])

smoker_no = 1 if smoker == "no" else 0
smoker_yes = 1 if smoker == "yes" else 0

input_data = pd.DataFrame({
    "age": [age],
    "bmi": [bmi],
    "children": [children],
    "smoker_no": [smoker_no],
    "smoker_yes": [smoker_yes]
})

if st.button("Predict"):
    result = model.predict(input_data)[0][0]
    st.success(f"Predicted Insurance Charge: ₹ {round(result,2)}")

st.write("**Accuracy** = 75%")
st.info("Built by Mirza Hussain Mazumder...")