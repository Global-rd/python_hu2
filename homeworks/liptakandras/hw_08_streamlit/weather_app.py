

import streamlit as st
import requests
import pandas as pd

@st.cache_data

def get_current_weather_data(city, api_key):

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)  # API válasz tárolásához
    data = response.json()  # json értelmezéséhez

    if response.status_code != 200:  # 200 a helyes érték
        st.warning(f"Error while retrieving info about {city}")
    else:
        return data
    

# Logika

def main():

    st.title("Current weather")
    api_key = st.secrets["weather"]["api_key"]
    city = st.text_input("Enter city:", "Budapest")
    weather_data = get_current_weather_data(city, api_key)

    if weather_data:

        st.header(f"Weather in {city}")

        col_1, col_2, col_3 = st.columns(3)

        with col_1:
            st.metric(label="Temperature (°C)", value=f"{weather_data['main']['temp']} °C")
        with col_2:
            st.metric(label="Humidity (%)", value=f"{weather_data['main']['humidity']} %")
        with col_3:
            st.metric(label="Wind Speed (m/s)", value=f"{weather_data['wind']['speed']} m/s")


        # Megjelenítés térképen

        st.header("City on the map")
        st.map(pd.DataFrame({"lon": [weather_data['coord']['lon']], "lat": [weather_data['coord']['lat']]}))


# Futtatás

if __name__ == "__main__":
    main()