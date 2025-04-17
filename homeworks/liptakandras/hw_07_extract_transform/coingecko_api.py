

import requests
import pandas

url = "https://api.coingecko.com/api/v3/coins/markets"

params = {"vs_currency": "usd",
          "order": "market_cap", # eszerint növekvő sorrend
          "per_page": 250,  # eredmények száma
          "page": 1}  # egy oldalon

response = requests.get(url=url, params=params)

data = response.json()
data_frames = pandas.DataFrame(data)

print("empty cells")
print(data_frames.isnull().sum())

market_cap_total = data_frames["market_cap"].sum()
print(f"Total market cap: {market_cap_total}")

top50_df = data_frames.sort_values(by="current_price", ascending=False).head(50)

top50_df = data_frames.sort_values(by="price_change_percentage_24h", ascending=False).head(50) 
    # itt nem tudom, kell-e új változó név, most nem adtam neki, tehát a meglévőt módosítom

def change_direction(pct):  # funkció if feltételekkel, amit később meghívhatok
    if pct > 0:
        return "+"
    elif pct < 0:
        return "-"
    else:
        return "0"
    
top50_df["change_direction"] = top50_df["price_change_percentage_24h"].apply(change_direction)
    # létrehozom az új oszlopot
    # alkalmazom a funkciót a "prince_change_percentage_24h" oszlopra