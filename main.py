import os
import streamlit as st
import requests

API_KEY = os.environ["API_KEY"]
headers = {"X-API-KEY": API_KEY}

country = input("Enter country name: ")
useryear = int(input("Enter year: "))
url = f"https://api.api-ninjas.com/v1/unemployment?country={country}"

request = requests.get(url, headers)
response = request.json()

for item in response:
    if item["year"] == useryear:
        print(item["unemployment_rate"])