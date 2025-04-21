import pandas as pd
import requests
import numpy as np

url = "https://api.coingecko.com/api/v3/coins/markets"
params = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 250,
    "page": 1,
    "price_change_percentage": "24h"
}

response = requests.get(url, params=params)

data = response.json()

df = pd.DataFrame(data)

df = df[["name", "symbol", "current_price", "market_cap", "price_change_percentage_24h"]]
print("-------------------------------------------------------")

#üres cellák
print("Empty cells per column:")
print(df.isnull().sum())
print("-------------------------------------------------------")

#total market cap
total_market_cap = df["market_cap"].sum()
print(f"\nTotal market cap: {total_market_cap:,.0f} USD")
print("-------------------------------------------------------")

#top 50 crypto
top50_df = df.sort_values(by="current_price", ascending=False).head(50).sort_values(by="price_change_percentage_24h", ascending=False)

conditions = [
    top50_df["price_change_percentage_24h"].isnull(),
    top50_df["price_change_percentage_24h"] > 0,
    top50_df["price_change_percentage_24h"] < 0,
    top50_df["price_change_percentage_24h"] == 0
]

values = ["NaN", "+", "-", "0"]

top50_df["change_direction"] = np.select(conditions, values, default="NaN")

print("\nTop 50 crypto:")
print(top50_df[["name", "current_price", "price_change_percentage_24h", "change_direction"]])









