"""
A következő feladatban a coinGecko public API-járól kell majd adatokat kinyerned, és ezeket elemezni Python segítségével.
A kövekező endpoint-ról “https://api.coingecko.com/api/v3/coins/markets” húzd le a 250 legnagyobb market cap-pel rendelkező kriptovalutát 
(értelmezd az api dokumentációt, két paramétert kell összesen használnod, és 1 api hívásból megszerezhető az adat). 
*market cap = kibocsátott darabszám * ár

Dokumentáció: https://docs.coingecko.com/reference/coins-markets 
(figyelj hogy itt a url-ben “pro-api.coingecko.com” szerepel, neked viszont simán “api.coingecko.com” kell, így regisztráció nélkül használhatod az api-t.

Tárold el ezeket egy dataframe-ben és oldd meg a következő feladatokat pandas segítségével:
1. Határozd meg, hogy a dataframe egyes oszlopaiban hány üres cella található és printeld ki.
2. Határozd meg a teljes dataframe-re a market_cap összegét és printeld ki.
3. Készíts egy új dataframe-et top50_df néven, itt csak az első 50 kriptovalutát tárold current_price alapján
4. Rendezd a top50_df-et price_change_percentage_24h alapján csökkenő sorrendbe!
5. Hozz létre egy új oszlopot a top50_df-be change_direction néven amelynek 3 értéke lehet :
a. Ha a price_change_percentage_24h értéke nagyobb mint 0, az oszlop értéke legyen “+”
b. Ha negatív, az oszlop értéke legyen “-“
c. Ha kereken 0, az érték legyen “0”
"""

import pandas as pd
import requests

# CoinGecko API elérési út
url = "https://api.coingecko.com/api/v3/coins/markets"

# Lekérdezési paraméterek
params = {
    'vs_currency': 'usd',                # USD alapú árak
    'order': 'market_cap_desc',          # Market cap szerint csökkenő sorrend
    'per_page': 250,                     # Maximum lekérhető: 250
    'page': 1                            # Csak az első oldalra van szükség
}

# API hívás
response = requests.get(url, params=params)

if response.status_code == 200:
    coins = response.json()
    df = pd.DataFrame(coins)

    # 1. Üres cellák száma oszloponként
    print("Hiányzó értékek az oszlopokban:")
    print(df.isnull().sum())

    # 2. Összesített piaci kapitalizáció
    total_market_cap = df['market_cap'].sum()
    print(f"\nÖsszesített Market Cap: {total_market_cap:,.0f} USD")

    # 3. Top 50 kriptovaluta kiválasztása (az első 50 sor az alap rendezés után)
    top50_df = df.iloc[:50].copy()

    # 4. Rendezzük price_change_percentage_24h alapján csökkenő sorrendbe
    top50_df.sort_values(by='price_change_percentage_24h', ascending=False, inplace=True)

    # 5. Új oszlop létrehozása: change_direction
    def irany(szazalek):
        if szazalek > 0:
            return '+'
        elif szazalek < 0:
            return '-'
        else:
            return '0'

    top50_df['change_direction'] = top50_df['price_change_percentage_24h'].apply(irany)

    # Csak néhány releváns adat megjelenítése a kimenetnél
    print("\nTop 10 kriptovaluta változási irány alapján:")
    print(top50_df[['id', 'symbol', 'current_price', 'price_change_percentage_24h', 'change_direction']].head(10))

else:
    print(f"Hiba történt az API hívás során. Státuszkód: {response.status_code}")
