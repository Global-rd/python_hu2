import requests
import pandas as pd

url = "https://api.coingecko.com/api/v3/coins/markets"
params = {
    "vs_currency": "usd",
    "per_page": 250,
}

response = requests.get(url=url, params=params)
data = response.json()

df = pd.DataFrame(data)

zero_cell = df.isnull().sum()
print("Number of zero cells: " + zero_cell)

market_cap = df["market_cap"].sum()
print(f"\nMarket cap: {market_cap:,.2f}")

top50_df = df.nlargest(50, "current_price")

top50_df = top50_df.sort_values(by="price_change_percentage_24h", ascending=False).reset_index(drop=True)

def direction_value(i):
    if i > 0:
        return "+"
    elif i < 0:
        return "-"
    else:
        return "0"

top50_df["change_direction"] = top50_df["price_change_percentage_24h"].apply(direction_value)

print("\nTop 50 crypto: " + top50_df.head())