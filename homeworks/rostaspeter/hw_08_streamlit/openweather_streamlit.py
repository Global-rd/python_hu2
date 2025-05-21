import streamlit as st
import requests
import pandas as pd
from datetime import datetime
import plotly.express as px

API_KEY = st.secrets["openweather"]["api_key"]

@st.cache_data(ttl=600)
def get_current_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    return response.json()

@st.cache_data(ttl=600)
def get_forecast(city):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    return response.json()

st.set_page_config(page_title="Weather Dashboard", layout="wide")

st.title("Weather Dashboard")
city = st.text_input("City Select", "Budapest")

if city:
    weather = get_current_weather(city)

    if weather.get("cod") != 200:
        st.error("Nem sikerült lekérni az adatokat. Ellenőrizd a város nevét.")
    else:
        st.subheader(f"Current Weather: {city}")
        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Temperature", f"{weather['main']['temp']} °C")
        with col2:
            st.metric("Wind Speed", f"{weather['wind']['speed']} m/s")
        with col3:
            st.metric("Humidity", f"{weather['main']['humidity']}%")

        st.subheader("5 day forecast")
        forecast = get_forecast(city)

        forecast_list = forecast["list"]
        data = {
            "Date": [datetime.fromtimestamp(item["dt"]) for item in forecast_list],
            "Temperature (°C)": [item["main"]["temp"] for item in forecast_list]
        }
        df = pd.DataFrame(data)

        fig = px.line(df, x="Date", y="Temperature (°C)", title="Temperature forecast")
        st.plotly_chart(fig, use_container_width=True)
