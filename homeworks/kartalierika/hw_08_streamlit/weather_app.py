import streamlit as st
import requests
import pandas as pd
from datetime import datetime
import sqlite3
import os
import plotly.express as px
from collections import defaultdict

# Loggolás SQLite adatbázisba
def log_to_db(city, temp, humidity, wind_speed):
    conn = sqlite3.connect("weather_logs.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS logs (
            city TEXT,
            temperature REAL,
            humidity INTEGER,
            wind_speed REAL,
            timestamp TEXT
        )
    """)

    cursor.execute("""
        INSERT INTO logs (city, temperature, humidity, wind_speed, timestamp)
        VALUES (?, ?, ?, ?, ?)
    """, (city, temp, humidity, wind_speed, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

    conn.commit()
    conn.close()

# Alap beállítások
st.set_page_config(page_title="Weather App", layout="centered")
api_key = st.secrets["weather"]["api_key"]

@st.cache_data
def get_current_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    return response.json()

@st.cache_data
def get_forecast(city):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    return response.json()

# Cím
st.title("🌤️ Robot Dreams Python - Weather Map & Data Visualization App")

# Város bekérése
city = st.text_input("Enter city name", "Budapest")

if city:
    data = get_current_weather(city)

    if data.get("cod") == 200:
        st.subheader(f" {city.title()}")

        
        weather_icon = data["weather"][0]["main"]
        emoji_map = {
            "Clear": "☀️",
            "Clouds": "☁️",
            "Rain": "🌧️",
            "Snow": "❄️",
            "Thunderstorm": "⛈️",
            "Drizzle": "🌦️",
            "Mist": "🌫️"
        }
        icon = emoji_map.get(weather_icon, "")
        st.write(f"Current weather: {weather_icon} {icon}")

        # KPI metrikák
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Temperature (°C)", f"{data['main']['temp']}°C")
        with col2:
            st.metric("Humidity (%)", f"{data['main']['humidity']}%")
        with col3:
            st.metric("Wind Speed (m/s)", f"{data['wind']['speed']} m/s")

        # Loggolás
        log_to_db(
            city=city,
            temp=data['main']['temp'],
            humidity=data['main']['humidity'],
            wind_speed=data['wind']['speed']
        )

        # Térkép
        st.subheader("City Map")
        lat, lon = data["coord"]["lat"], data["coord"]["lon"]
        st.map(pd.DataFrame({"lat": [lat], "lon": [lon]}))

        # Hőmérséklet előrejelzés
        forecast_data = get_forecast(city)
        if forecast_data.get("cod") == "200":
            st.subheader("Temperature Trends (Next 5 Days)")
            forecast_list = forecast_data["list"]

            times = [item["dt_txt"] for item in forecast_list]
            temps = [item["main"]["temp"] for item in forecast_list]

            df_forecast = pd.DataFrame({
                "Date": pd.to_datetime(times),
                "Temperature": temps
            }).set_index("Date")

            fig_temp = px.line(
                df_forecast,
                x=df_forecast.index,
                y="Temperature",
                title="Temperature Forecast (5 Days)",
                template="plotly_white",
                markers=True,
                color_discrete_sequence=["#a855f7"]
            )
            st.plotly_chart(fig_temp, use_container_width=True)

    else:
        st.warning("City not found. Please try another valid city name.")

# Logok megjelenítése
if os.path.exists("weather_logs.db"):
    st.subheader(" Search Log")
    conn = sqlite3.connect("weather_logs.db")
    df_logs = pd.read_sql_query("SELECT * FROM logs ORDER BY timestamp DESC", conn)
    conn.close()
    st.dataframe(df_logs)

# Csapadék valószínűsége
daily_rain_prob = defaultdict(int)

for item in forecast_list:
    date = item["dt_txt"].split(" ")[0]  
    pop = item.get("pop", 0)
    daily_rain_prob[date] = max(daily_rain_prob[date], pop)

st.subheader("Precipitation probability (next 5 days)")

for date, pop in daily_rain_prob.items():
    percent = int(pop * 100)
    drops = "💧" * (percent // 10)
    st.markdown(f"**{date}** – {percent}% {drops}")


#Min-Max hőmérséklet
daily_minmax = defaultdict(lambda: {"min": float("inf"), "max": float("-inf")})

for item in forecast_list:
    date = item["dt_txt"].split(" ")[0]  
    temp_min = item["main"]["temp_min"]
    temp_max = item["main"]["temp_max"]

    
    if temp_min < daily_minmax[date]["min"]:
        daily_minmax[date]["min"] = temp_min
    if temp_max > daily_minmax[date]["max"]:
        daily_minmax[date]["max"] = temp_max

st.subheader("Daily minimum-maximum temperature")

for date, temps in sorted(daily_minmax.items()):
    st.markdown(f"**{date}** – Min: `{temps['min']}°C` | Max: `{temps['max']}°C`")

# Top 5 keresett város 
st.subheader("Top 5 Searched Cities")
conn = sqlite3.connect("weather_logs.db")
df_top = pd.read_sql_query("""
    SELECT city, COUNT(*) as search_count
    FROM logs
    GROUP BY city
    ORDER BY search_count DESC
    LIMIT 5
""", conn)
conn.close()

for index, row in df_top.iterrows():
    st.markdown(f"**{index + 1}. {row['city']}** — {row['search_count']} search")

