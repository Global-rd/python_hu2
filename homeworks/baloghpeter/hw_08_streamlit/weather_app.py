import streamlit as st
import requests
from datetime import datetime
import pandas as pd

st.set_page_config(page_title="Időjárás App", layout="wide")

API_KEY = st.secrets["cb808fe1c70d5ccae85de294de6562ba"]

@st.cache_data(ttl=600)
def get_current_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=hu"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

st.sidebar.title("🌍 Város kiválasztása")
city = st.sidebar.text_input("Add meg a város nevét:", "Budapest")

data = get_current_weather(city)

if data:
    st.title(f"☁️ Időjárás jelenleg: {city}")

    col1, col2, col3 = st.columns(3)
    col1.metric("🌡️ Hőmérséklet (°C)", f"{data['main']['temp']}°C")
    col2.metric("💧 Páratartalom", f"{data['main']['humidity']}%")
    col3.metric("💨 Szélsebesség", f"{data['wind']['speed']} m/s")

    lat = data['coord']['lat']
    lon = data['coord']['lon']
    map_df = pd.DataFrame({'lat': [lat], 'lon': [lon]})
    st.map(map_df, zoom=10)

    description = data['weather'][0]['description'].capitalize()
    icon_url = f"http://openweathermap.org/img/wn/{data['weather'][0]['icon']}@2x.png"
    st.markdown(f"### {description}")
    st.image(icon_url)

else:
    st.warning("Nem sikerült lekérni az időjárási adatokat. Ellenőrizd a város nevét.")

#közben rájöttem, hogy rossz repoba nyomtam