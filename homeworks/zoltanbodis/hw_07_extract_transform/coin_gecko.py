import requests
import settings as s
import pandas as pd

url = f"{s.API_BASE_URL}{s.PATH_COINMARKETS}"
params = {"vs_currency":s.VS_CURRENCY,
          "order": s.ORDER,
          "per_page": s.RESULTS_PER_PAGE}

df = pd.DataFrame(requests.get(url=url, params=params).json())
#print(df.head())

#1. Határozd meg, hogy a dataframe egyes oszlopaiban hány üres cella található és printeld ki.
print("\n\n----------------")
empty_cells = df.isna().sum()
print(empty_cells)

#2. Határozd meg a teljes dataframe-re a market_cap összegét és printeld ki.
print("----------------")
sum_market_cap = df["market_cap"].sum()
print(f" {sum_market_cap:,.0f}")

#3. Készíts egy új dataframe-et top50_df néven, itt csak az első 50 kriptovalutát tárold current_price alapján
print("----------------")
top50_df = df.sort_values(by="current_price", ascending=False).head(50)
print(top50_df.head())

#4. Rendezd a top50_df-et price_change_percentage_24h alapján csökkenő sorrendbe!
top50_df = top50_df.sort_values(by="price_change_percentage_24h", ascending=False)

"""
5. Hozz létre egy új oszlopot a top50_df-be change_direction néven amelynek 3
értéke lehet:
   a. Ha a price_change_percentage_24h értéke nagyobb mint 0, az oszlop
      értéke legyen "+"
   b. Ha negatív, az oszlop értéke legyen "-"
   c. Ha kereken 0, az érték legyen "0"
"""
def change_direction(row):
    if row["price_change_percentage_24h"] > 0:
        return "+"
    elif row["price_change_percentage_24h"] < 0:
        return "-"
    else:
        return "0"

print("----------------")
top50_df["change_direction"] = top50_df.apply(change_direction, axis=1)
print(top50_df[["symbol", "name", "price_change_percentage_24h", "change_direction"]])