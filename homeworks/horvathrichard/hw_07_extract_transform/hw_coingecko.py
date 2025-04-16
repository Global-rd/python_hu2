import requests
import pandas as pd

#1. adatok letöltése (2 paraméterrel)
url = "https://api.coingecko.com/api/v3/coins/markets"
params = {
    "vs_currency": "usd",  # kötelező paraméter: usd legyen a kripto megfelelő valutája
    "per_page": 250        # az api limit(100/oldal) miatt ezt meg kell növelni
}

response = requests.get(url, params=params)
data = response.json()

#2. dataFrame létrehozása és market_cap szerinti rendezés
df = pd.DataFrame(data)
df = df.sort_values(by="market_cap", ascending=False).reset_index(drop=True)

#3. üres cellák számolása oszloponként
print("Üres cellák száma oszloponként:")
print(df.isnull().sum())

#4. összesített market_cap
total_market_cap = df["market_cap"].sum()
print("\nTeljes market cap összege:")
print(f"${total_market_cap:,.2f}")

#5. top50_df létrehozása current_price szerint
top50_df = df.sort_values(by="current_price", ascending=False).head(50)

#6. rendezd a top50_df-et 24 órás változás szerint csökkenően
top50_df = top50_df.sort_values(by="price_change_percentage_24h", ascending=False)

#7. change_direction oszlop hozzáadaás
def get_change_direction(change):
    if pd.isnull(change):
        return "?"
    elif change > 0:
        return "+"
    elif change < 0:
        return "-"
    else:
        return "0"

top50_df["change_direction"] = top50_df["price_change_percentage_24h"].apply(get_change_direction)

#8. eredmény kiíratása
print("\nTop 50 coin 24 órán belüli változás szerint:")
print(top50_df[["name", "current_price", "price_change_percentage_24h", "change_direction"]])
