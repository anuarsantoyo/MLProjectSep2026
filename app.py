# https://docs.streamlit.io/develop/api-reference
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt






df = pd.read_csv("data/data_cleaned.csv")

st.write("# My Project")
st.write("---")


a =  st.number_input("pick a number")
b = 2
c = a+b
st.write(c)


if c > 50:
    st.write("to large!!!!")


col1, col2 = st.columns(2)

with col1:
    st.write("dsfgdsf"*100)

with col2:
    row = int(c)
    st.write(df[:row])
    st.write("sadfsdafdsafdsa")
    color = st.color_picker("Pick A Color", "#00f900")
    figure = df[:row]["age"].plot(color = color).get_figure()
    st.write(figure)



with st.sidebar:
    st.write("# Title")
    st.write("sdf"*100)


import streamlit as st

st.html("""
    <style>
        .big-font { font-size: 32px; color: #1f77b4; font-weight: bold; }
    </style>
    <p class="big-font">Hello, styled world!</p>
""")