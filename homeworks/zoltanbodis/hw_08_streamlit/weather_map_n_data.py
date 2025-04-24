import streamlit as st
import pandas as pd
import requests
import plotly.express as px
import datetime
import settings as s

@st.cache_data(ttl=86400)
def get_current_weather(city):
    print(f"Get weather for {city}")

    pass