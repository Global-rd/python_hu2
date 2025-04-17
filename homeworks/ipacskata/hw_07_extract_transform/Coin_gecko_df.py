import requests 
import pandas as pd


url = "https://api.coingecko.com/api/v3/coins/markets"


params = {
    "vs_currency": "usd",
    "per_page": 250,
    "order": "market_cap_desc"
}

response = requests.get(url=url, params=params)
print(response.status_code)


data = response.json()

df=pd.DataFrame(data)
print(df)

print(df.info())
print("Empty cells:")
print(df.isnull().sum())

sum_market_cap= df["market_cap"].sum()
print(sum_market_cap)
print(df.columns)
top50_df = df.sort_values("current_price", ascending=False)
print(top50_df.head(50)) 
price_change_percentage_df = top50_df.sort_values("price_change_percentage_24h", ascending=True).head(50) 

def change_direction(row):
    if row["price_change_percentage_24h"] > 0:
        return "+"
    elif row["price_change_percentage_24h"] < 0:
        return "-"
    else:
        return "0"
top50_df["change direction"] = top50_df.apply(change_direction, axis=1)
print(top50_df)    