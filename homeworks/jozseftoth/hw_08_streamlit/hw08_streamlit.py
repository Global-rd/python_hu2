import streamlit as st
import pandas as pd
import requests
import plotly.express as px
import datetime
import plotly.graph_objects as go

API_KEY=st.secrets["openweather"]["openweather_api_key"]

st.set_page_config(
    page_title="Weather App",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.sidebar.title("Enter a city name and country code")

city_name = st.sidebar.text_input("City:", "Sárosd")
country_code = st.sidebar.text_input("Country code (example: HU):", "HU")

@st.cache_data(ttl=600)
def get_weather(city, country, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid={api_key}&units=metric"
    response = requests.get(url)
    return response.json()

data = get_weather(city_name, country_code, API_KEY)

#check the response status code
if data.get("cod") != 200:
    st.warning(f"Failure at**{city_name}, {country_code}** download: {data.get('message', 'Unknown error')}')")
    st.stop()

#required data  
temp = data["main"]["temp"]
feels_like = data["main"]["feels_like"]
humidity = data["main"]["humidity"]
wind_speed = data["wind"]["speed"]
desc = data["weather"][0]["description"].capitalize()
icon = data["weather"][0]["icon"]
lat = data["coord"]["lat"]
lon = data["coord"]["lon"]
timestamp = datetime.datetime.fromtimestamp(data["dt"])

#top section
st.title(f"Current weather in: {city_name}, {country_code}")
st.caption(f"refreshed: {timestamp.strftime('%Y-%m-%d %H:%M:%S')}")

#az időjárás jellemzői
st.subheader(f"Current weather: {desc}")
st.image(f"http://openweathermap.org/img/wn/{icon}@2x.png", width=100)

st.markdown("---")
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric(label="Temperature", value=f"{temp} °C")
with col2:
    # Szélirány meghatározása
    wind_deg = data["wind"]["deg"]  # Szélirány fokokban

    # Szélirány szöveges meghatározása
    def get_wind_direction(deg):
        if 337.5 <= deg <= 360 or 0 <= deg < 22.5:
            return "N"  # Észak
        elif 22.5 <= deg < 67.5:
            return "NE"  # Északkelet
        elif 67.5 <= deg < 112.5:
            return "E"  # Kelet
        elif 112.5 <= deg < 157.5:
            return "SE"  # Délkelet
        elif 157.5 <= deg < 202.5:
            return "S"  # Dél
        elif 202.5 <= deg < 247.5:
            return "SW"  # Délnyugat
        elif 247.5 <= deg < 292.5:
            return "W"  # Nyugat
        elif 292.5 <= deg < 337.5:
            return "NW"  # Északnyugat

    wind_direction = get_wind_direction(wind_deg)

    # dinamic compass SVG
    compass_svg = f"""
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="50" height="50">
    <circle cx="50" cy="50" r="45" stroke="black" stroke-width="2" fill="white" />
    <line x1="50" y1="50" x2="50" y2="10" stroke="red" stroke-width="2" transform="rotate({wind_deg}, 50, 50)" />
    <text x="50" y="95" font-size="10" text-anchor="middle" fill="black">N</text>
</svg>
"""

# wind speed and direction
with col2:
    st.metric(label="Wind speed", value=f"{wind_speed} m/s")
    st.caption(f"Direction: {wind_direction} ({wind_deg}°)")
    st.markdown(compass_svg, unsafe_allow_html=True)
with col3:
    st.metric(label="Feels like", value=f"{feels_like} °C")
with col4:
    st.metric(label="Humidity", value=f"{humidity} %")


st.markdown("---")


# Bar charts for temperature and feels like
col1, col2 = st.columns(2)

# Color function for temperature and feels like
def get_color(value):
    if -30 <= value <= 5:
        return "#ADD8E6"  # light blue
    elif 5 < value <= 15:
        return "#FFFF00"  # yellow
    elif 15 < value <= 25:
        return "#FFA500"  # orange
    elif value > 25:
        return "#FF0000"  # red 
    return "#FFFFFF"  # default white for out of range

with col1:
    st.subheader("Temperature")
    fig1 = px.bar(
        x=["temperature in: °C"],
        y=[temp],
        labels={"x": "", "y": ""},
        title="current temperature",
        text_auto=True
    )
    fig1.update_traces(
        marker_color=get_color(temp),
        textfont_size=10,
        width=0.2  # column width
    )
    fig1.update_layout(
        height=300,
        margin=dict(t=30, b=10),
        yaxis=dict(range=[-30, 50])  # Min  -30, max 50
    )
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    st.subheader("Feels like")
    fig2 = px.bar(
        x=["temperature in: °C"],
        y=[feels_like],
        labels={"x": "", "y": ""},
        title="current temperature",
        text_auto=True
    )
    fig2.update_traces(
        marker_color=get_color(feels_like),
        textfont_size=10,
        width=0.2  # column width
    )
    fig2.update_layout(
        height=300,
        margin=dict(t=30, b=10),
        yaxis=dict(range=[-30, 50])  # Minimum -30, maximum 50
    )
    st.plotly_chart(fig2, use_container_width=True)

st.markdown("---")


#MAP
st.subheader(f" {city_name}, {country_code} location")
st.map([{"lat": lat, "lon": lon}])

# 5 napos előrejelzés lekérése
@st.cache_data(ttl=600)
def get_forecast(city, country, api_key):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city},{country}&appid={api_key}&units=metric"
    response = requests.get(url)
    return response.json()

forecast_data = get_forecast(city_name, country_code, API_KEY)

# Ellenőrzés, hogy az előrejelzés sikeres-e
if forecast_data.get("cod") != "200":
    st.warning(f"Failed to fetch forecast data for {city_name}, {country_code}: {forecast_data.get('message', 'Unknown error')}")
else:
    # Adatok feldolgozása
    forecast_timestamps = [datetime.datetime.fromtimestamp(item["dt"]) for item in forecast_data["list"]]
    forecast_temperatures = [item["main"]["temp"] for item in forecast_data["list"]]

    # Vonaldiagram megjelenítése
    st.subheader("5-Day Temperature Forecast")
    fig = px.line(
        x=forecast_timestamps,
        y=forecast_temperatures,
        labels={"x": "Date and Time", "y": "Temperature (°C)"},
        title="5-Day Temperature Forecast"
    )
    fig.update_traces(line_color="blue", line_width=2)
    fig.update_layout(
        height=400,
        margin=dict(t=30, b=10),
        xaxis=dict(title="Date and Time", tickformat="%Y-%m-%d %H:%M"),
        yaxis=dict(title="Temperature (°C)")
    )
    st.plotly_chart(fig, use_container_width=True)


