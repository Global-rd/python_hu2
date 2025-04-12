import requests
import pandas as pd

#1. adatok letöltése
url = "https://api.coingecko.com/api/v3/coins/markets"
params = {
    "vs_currency": "usd",  # kötelező paraméter: usd legyen a kripto megfelelő valutája
}

response = requests.get(url, params=params)
data = response.json()