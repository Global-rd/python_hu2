import streamlit as st
import pandas as pd
import requests
import plotly.express as px
import datetime 

API_KEY=st.secrets["openweather"]["api_key"]
BASE_URL_ACTUAL="https://api.openweathermap.org/data/2.5/weather?q="
BASE_URL_FORECAST="https://api.openweathermap.org/data/2.5/forecast?q="

@st.cache_data(ttl=86400)
def actual_wheather_in_city(city):
    print(f"Actual city : {city}")

    url = f"{BASE_URL_ACTUAL}{city}&appid={API_KEY}&units=metric"
    print(url)
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"Hibás adatok: {response.status_code} - {response.text}")


st.title("Robot Dreams Python - Weather Map & Data Visualization App")
st.subheader("Made by Soma")

city = st.text_input("Enter City name: ", "Budapest")

data = actual_wheather_in_city(city)



