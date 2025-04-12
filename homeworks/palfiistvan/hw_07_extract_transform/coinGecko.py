import requests
import pandas as pd

# Call API:
url = "https://api.coingecko.com/api/v3/coins/markets"
params = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 250,
    "page": 1,
}

response = requests.get(url, params=params)
data = response.json()

# Convert to DataFrame:
df = pd.DataFrame(data)


# 1. Határozd meg, hogy a dataframe egyes oszlopaiban hány üres cella található
missing_values = df.isnull().sum()
print(f"Missing values / Column:\n, {missing_values}")

# 2. Határozd meg a teljes dataframe-re a market_cap összegét
total_market_cap = df["market_cap"].sum()
print(f"Total market cap amount: ${total_market_cap:,.2f}")

# 3. Készíts új dataframe-et top50_df néven, az első 50 kriptó current_price alapján
top50_df = df.sort_values("current_price", ascending=False).head(50)

# 4. Rendezd a top50_df-et price_change_percentage_24h alapján csökkenő sorrendbe
top50_df = top50_df.sort_values("price_change_percentage_24h", ascending=False)

# 5. Hozz létre egy új oszlopot a top50_df-be change_direction néven amelynek 3 értéke lehet
def change_direction(change):
    if pd.isna(change):
        return "0"
    elif change > 0:
        return "+"
    elif change < 0:
        return "-"
    else:
        return "0"
    
top50_df["change_direction"] = top50_df["price_change_percentage_24h"].apply(change_direction)

print("------------------------------------------------------------------------------------------------")
print("Top 10 coins by direction of change:")
print(top50_df[["name", "current_price", "price_change_percentage_24h", "change_direction"]].head(10))