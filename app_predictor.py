import streamlit as st
import pandas as pd

import joblib

# Load
pipeline = joblib.load('pipeline.joblib')

age = st.number_input("Your age")
df = pd.DataFrame({"C4":[2], "age":[age], "A4":[3], "gender":["Male"] ,"N1":[2], "N2":[3], "N3":[3], "N4":[4], "N5":[1], "N6":[2], "N7":[1], "N8":[1], "E10":[3], "hand":["Right"],"N9":[2], "N10": [1], "E1": [5], "E3":[3], "E4":[2], "E5":[1], "E7":[4], "E9":[3]})
prediction = pipeline.predict(df)


st.write(prediction)