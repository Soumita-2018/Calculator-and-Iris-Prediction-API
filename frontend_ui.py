import streamlit as st
import json
import requests

st.title("Basic calculator App")

option = st.selectbox('What operation you want to perform?',{'addition', 'subtraction', 'multiplication', 'division'})

st.write(" ")

st.write("Select the number from slider below")

x = st.slider("x", 0, 100, 20)
y = st.slider("y", 0, 130, 10)
inputs={"operation":option, "x":x, "y": y}

if st.button('calculate'):
    res = requests.post(url = 'http://localhost:8000/calculate', data=json.dumps(inputs))
    st.subheader(f"response from calculator API {res.text}")