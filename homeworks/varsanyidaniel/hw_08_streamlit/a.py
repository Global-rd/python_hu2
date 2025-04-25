import streamlit as st
import pandas as pd
import requests
import plotly.express as px

API_KEY = st.secrets["polygon"]["api_key"]

@st.cache_data(ttl=3600)
def collect_data(city, API_KEY):
    url=f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    response=requests.get(url)
    data=response.json()
    if response.status_code == 200:
        return data
    else:
        st.error(f"Failed to fetch data. Error: {response.status_code}")

st.title("Robot Dreams Python - Weather Map & Data Visualization App")

city=st.sidebar.text_input("Enter city name:")

data = collect_data(city)