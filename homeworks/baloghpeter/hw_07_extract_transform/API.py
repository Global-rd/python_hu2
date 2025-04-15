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

print("Hiányzó értékek száma oszloponként:")
print(df.isnull().sum())


total_market_cap = df["market_cap"].sum()
print(f"\nÖsszesített market_cap érték: {total_market_cap:,} USD")

top50_df = df.sort_values(by="current_price", ascending=False).head(50)

top50_df = top50_df.sort_values(by="price_change_percentage_24h", ascending=False)

def get_change_direction(change):
    if change > 0:
        return "+"
    elif change < 0:
        return "-"
    else:
        return "0"

top50_df["change_direction"] = top50_df["price_change_percentage_24h"].apply(get_change_direction)

print("\nTop 5 érme a change_direction szerint:")
print(top50_df[["name", "current_price", "price_change_percentage_24h", "change_direction"]].head())

top50_df.to_excel("top50_crypto.xlsx", index=False)

print("\nA top50_df sikeresen elmentve Excel fájlba: top50_crypto.xlsx")

