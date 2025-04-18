import requests
import pandas as pd

url = "https://api.coingecko.com/api/v3/coins/markets"
params = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 250,
    "page": 1
}

response = requests.get(url, params=params)
data = response.json()

df = pd.DataFrame(data)

# üres cellák száma a dataframe egyes oszlopaiban
print(df.isnull().sum())

# a teljes dataframe-re a market_cap összege
total_market_cap = df["market_cap"].sum()
print(f"The total market cap value: {total_market_cap:,} USD")

# az első 50 kriptovaluta current_price alapján
top50_df = df.sort_values(by="current_price", ascending=False).head(50).copy()

# price_change_percentage_24h alapján csökkenő sorrend
top50_df = top50_df.sort_values(by="price_change_percentage_24h", ascending=False)

# change_direction oszlop hozzáadása
def change_direction(value):
    if value > 0:
        return "+"
    elif value < 0:
        return "-"
    else:
        return "0"

top50_df["change_direction"] = top50_df["price_change_percentage_24h"].apply(change_direction)