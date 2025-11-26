import os
import streamlit as st
import requests

API_KEY = st.secrets["API_KEY"]
headers = {"X-API-KEY": API_KEY}

st.title("Unemployment Rate Per Year per Country")
st.write("Given country and a year, display unemployment rate")
st.divider()

country = st.text_input("Country: ")
useryear = st.number_input("Year: ", step = 1, min_value = 1980, max_value =2029)
submit = st.button("Submit")
if submit:
    url = f"https://api.api-ninjas.com/v1/unemployment?country={country}"

    request = requests.get(url, headers)
    response = request.json()

    for item in response:
        if item["year"] == useryear:
            st.subheader(f"THe unemployment rate is {item['unemployment_rate']}%")