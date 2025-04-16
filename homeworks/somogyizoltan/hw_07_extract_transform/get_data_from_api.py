"""
A kövekező endpoint-ról “https://api.coingecko.com/api/v3/coins/markets” húzd le
a 250 legnagyobb market cap-pel rendelkező kriptovalutát (értelmezd az api
dokumentációt, két paramétert kell összesen használnod, és 1 api hívásból
megszerezhető az adat). *market cap = kibocsátott darabszám * ár
Dokumentáció: https://docs.coingecko.com/reference/coins-markets (figyelj hogy itt
a url-ben “pro-api.coingecko.com” szerepel, neked viszont simán
“api.coingecko.com” kell, így regisztráció nélkül használhatod az api-t.
Tárold el ezeket egy dataframe-ben és oldd meg a következő feladatokat pandas
segítségével:
1. Határozd meg, hogy a dataframe egyes oszlopaiban hány üres cella található
és printeld ki.
2. Határozd meg a teljes dataframe-re a market_cap összegét és printeld ki.
3. Készíts egy új dataframe-et top50_df néven, itt csak az első 50 kriptovalutát
tárold current_price alapján
4. Rendezd a top50_df-et price_change_percentage_24h alapján csökkenő
sorrendbe!
5. Hozz létre egy új oszlopot a top50_df-be change_direction néven amelynek 3
értéke lehet :
a. Ha a price_change_percentage_24h értéke nagyobb mint 0, az oszlop
értéke legyen “+”
b. Ha negatív, az oszlop értéke legyen “-“
c. Ha kereken 0, az érték legyen “0”
"""


import requests
import pandas as pd


# USD-ben veszem el az árakat, de ahogy láttam szinte bármilyen valutát tud hozni - a leírás szerint van egy olyan változó is, amiben  market_cap helyezés is ott van
url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&per_page=250&market_cap_rank<=250"

headers = {"accept": "application/json"}

response = requests.get(url, headers=headers)

# Adat transformálás DataFrame-be

data_from_api = response.json()
df = pd.DataFrame(data_from_api)


# 1. Határozd meg, hogy a dataframe egyes oszlopaiban hány üres cella található és printeld ki.

empty_cells_in_df = df.isnull().sum()
print("Az üres cellák száma oszloponként:")
print(empty_cells_in_df)


# 2. Határozd meg a teljes dataframe-re a market_cap összegét és printeld ki.

total_market_cap = df["market_cap"].sum()
print(f"A teljes piaci kapitalizáció értéke a top 250 legnagyobb terméknek: {total_market_cap:,.0f} USD\n")


# 3. Készíts egy új dataframe-et top50_df néven, itt csak az első 50 kriptovalutát tárold current_price alapján

top50_df = df.sort_values(by="current_price", ascending=False).head(50)


# 4. Rendezd a top50_df-et price_change_percentage_24h alapján csökkenő sorrendbe!

top50_df = top50_df.sort_values(by="price_change_percentage_24h", ascending=False)


# 5. Új oszlop - napi változások kimutatása

def daily_change(row):
    if row["price_change_percentage_24h"] > 0:
        return "+"
    elif row["price_change_percentage_24h"] < 0:
        return "-"
    else:
        return "0"

top50_df['change_price_daily'] = top50_df.apply(daily_change, axis=1)

print("Top 50 legnagyobb árú termék napi változásainak kimutatása:\n")
print(top50_df[["name", "current_price", "market_cap", "market_cap_rank", "price_change_percentage_24h", "change_price_daily"]])