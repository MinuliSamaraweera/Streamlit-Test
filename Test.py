# app.py
import streamlit as st
import numpy as np
import pandas as pd

st.write("## Test")

st.link_button("Profile",url="/Profile")
st.link_button("Dashboard",url="/Dashboard")

st.write("Hello, world!")

name = st.text_input("What is your name")

st.write(f"My name is {name}")

is_clicked = st.button("Click me")

data = pd.read_csv("demographic_data_dataset.csv")
st.write(data)

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["a", "b", "c"]
)
st.bar_chart(chart_data)
st.line_chart(chart_data)
