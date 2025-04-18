
import requests
import pandas as pd

url = "https://api.coingecko.com/api/v3/coins/markets"



params = {"vs_currency": "usd",   #others are by default
          "per_page": 250,  
          } 

response = requests.get(url=url, params=params)

data = response.json()

df = pd.DataFrame(data)
print(df)

zero_values = df.isnull().sum()
print("Zero values per column:\n", zero_values)
print("--------------------------")

market_cap_total = df["market_cap"].sum()
print(f"TOTAL market cap: {market_cap_total}")
print("---------------------------")


top50_df = df.sort_values(by="current_price", ascending=False).head(50)


top50_df = df.sort_values(by="price_change_percentage_24h", ascending=False)




def change_direction(price_change_percentage_24h):  
    if price_change_percentage_24h > 0:
        return "+"
    elif price_change_percentage_24h < 0:
        return "-"
    else:
        return "0"

top50_df["change_direction"] = top50_df["price_change_percentage_24h"].apply(change_direction)
  
#print(top50_df)

