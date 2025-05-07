import requests
import pandas as pd

# Lekérjük az adatokat
url = "https://api.coingecko.com/api/v3/coins/markets"
paramok = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 250,
    "page": 1
}

# Lekérjük az adatokat, json
valasz = requests.get(url, params=paramok)
adatok = valasz.json()

# Pandas
df = pd.DataFrame(adatok)

# 1. feladat – üres cellák száma
print("Üres cellák (null értékek) oszloponként:")
uresek = df.isnull().sum()
print(uresek)

# 2. feladat – teljes market cap összeg
ossz_marketcap = df['market_cap'].sum()
print("Az összes market cap összege:")
print(ossz_marketcap)

# 3. feladat – új df top50_df current_price szerint
top50_df = df.sort_values("current_price", ascending=False).head(50)

# 4. feladat – price_change_percentage_24h szerint rendezés csökkenőbe
top50_df = top50_df.sort_values("price_change_percentage_24h", ascending=False)

# 5. feladat – új oszlop change_direction
def valtozas_irany(szam):
    if pd.isnull(szam):
        return "N/A"  # nincs adat, pl. új coin
    if szam > 0:
        return "+"
    elif szam < 0:
        return "-"
    else:
        return "0"

top50_df["change_direction"] = top50_df["price_change_percentage_24h"].apply(valtozas_irany)

# Ellenőrzés
print("Top 5 coin változással:")
print(top50_df[["id", "current_price", "price_change_percentage_24h", "change_direction"]].head())