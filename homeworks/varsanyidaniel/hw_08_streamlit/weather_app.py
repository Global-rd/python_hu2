import streamlit as st
import pandas as pd
import requests

API_KEY=st.secrets["weatherapp"]["apikey"].toml


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

city=st.sidebar.text_input("Enter city name:", "London")

data = collect_data(city, API_KEY)

if data:
    st.header(f"Current Weather in {city}:")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="Temperature (°C)", value=f"{data['main']['temp']} °C")
    with col2:
        st.metric(label="Humidity (%)", value=f"{data['main']['humidity']} %")
    with col3:
        st.metric(label="Wind Speed (m/s)", value=f"{data['wind']['speed']} m/s")
    st.header("Weather Map")
    st.map(pd.DataFrame({"lon": [data['coord']['lon']], "lat": [data['coord']['lat']]}))

print(data)

# streamlit run homeworks/varsanyidaniel/hw_08_streamlit/weather_app.py