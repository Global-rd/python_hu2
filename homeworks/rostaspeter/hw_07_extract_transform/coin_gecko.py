import requests
import pandas as pd

url = "https://api.coingecko.com/api/v3/coins/markets"
params = {
    "vs_currency": "usd",
    "per_page": 250
}

response = requests.get(url, params=params)
data = response.json()

df = pd.DataFrame(data)
df = df.sort_values(by="market_cap", ascending=False).reset_index(drop=True)

print("Üres cellák:")
print(df.isnull().sum())

total_market_cap = df["market_cap"].sum()
print("\nTeljes összeg:")
print(f"${total_market_cap:,.2f}")

top50_df = df.sort_values(by="current_price", ascending=False).head(50)

top50_df = top50_df.sort_values(by="price_change_percentage_24h", ascending=False)

def change_direction(change):
    if pd.isnull(change):
        return "?"
    elif change > 0:
        return "+"
    elif change < 0:
        return "-"
    else:
        return "0"

top50_df["change_direction"] = top50_df["price_change_percentage_24h"].apply(change_direction)

print("\nTop 50 coin:")
print(top50_df[["name", "current_price", "price_change_percentage_24h", "change_direction"]])