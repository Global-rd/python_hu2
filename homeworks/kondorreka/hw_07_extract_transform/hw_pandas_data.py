"""Tárold el ezeket egy dataframe-ben és oldd meg a következő feladatokat pandas
segítségével:
"""
from def_crypto_data_api import crypto_data #api függvény import
import pandas as pd
import sys
from def_direction import direction

try:
    crypto = pd.DataFrame(crypto_data()) #Pandas DataFrame létrehozása
except Exception as e:
    print(f'Hiba: {e}')

    sys.exit() #kilépés a programból
          
print(crypto.head())
print(crypto.describe())
print(crypto.info())
print("-------------------------------------------------")

"""
1. Határozd meg, hogy a dataframe egyes oszlopaiban hány üres cella található
és printeld ki.
"""
empty_cells = crypto.isna().sum().sort_values(ascending = False)
print(f'1. Oszlopokban található  üres cellák száma: \n'
      f'{empty_cells}')
print("-------------------------------------------------")

"""
2. Határozd meg a teljes dataframe-re a market_cap összegét és printeld ki.
"""
sum_market_cap = crypto['market_cap'].sum()

print(f'2. A market_cap összege: {sum_market_cap:,.0f} USD.')
print("-------------------------------------------------")

"""
3. Készíts egy új dataframe-et top50_df néven, itt csak az első 50 kriptovalutát
tárold current_price alapján
"""
crypto_sorted_current_price = crypto.sort_values('current_price', ascending = False).reset_index(drop=True)

top50_df = crypto_sorted_current_price.iloc[0:50].reset_index(drop=True)
#print(top50_df.head())
#print(top50_df.tail())
#print(len(top50_df))

"""
4. Rendezd a top50_df-et price_change_percentage_24h alapján csökkenő
sorrendbe!
"""
top50_df = top50_df.sort_values('price_change_percentage_24h', ascending = False).reset_index(drop=True)

#print(top50_df.columns)
#print(top50_df[['id', 'symbol', 'name', 'price_change_percentage_24h']].head())
#print(top50_df[['id', 'symbol', 'name', 'price_change_percentage_24h']].tail())

"""
5. Hozz létre egy új oszlopot a top50_df-be change_direction néven amelynek 3
értéke lehet :
a. Ha a price_change_percentage_24h értéke nagyobb mint 0, az oszlop
értéke legyen “+”
b. Ha negatív, az oszlop értéke legyen “-“
c. Ha kereken 0, az érték legyen “0”
"""
print(f'Egyedi árváltozás % értékek: \n'
     f'{top50_df['price_change_percentage_24h'].unique()}')
print("-------------------------------------------------")
empty_price_change_percentage_24h = top50_df[top50_df['price_change_percentage_24h'].isna()]
empty_price_change_percentage_24h = empty_price_change_percentage_24h[['current_price', 'price_change_24h', 'price_change_percentage_24h']]

# előző napi ár = current_price - price_change_24h
#  változás %-ban = 8current_price / előző napi ár) - 1

#ellenőrzöm hogy ki tudom-e számolni
print(f'Számoláshoz szükséges értékek: \n'
    f"{empty_price_change_percentage_24h}")
print("-------------------------------------------------")

#mivel nem áll rendelkezésre adat amiből ki tudom számolni, átlagot használok
average_price_change_percentage_24h = top50_df['price_change_percentage_24h'].mean()

#üres cellák feltöltése átlaggal
top50_df['price_change_percentage_24h'] = top50_df['price_change_percentage_24h'].fillna(average_price_change_percentage_24h)

#ellenőrzöm az értékeket

print(f'Egyedi értékek árváltozás % hiányzó értékének feltöltése után: \n'
    f'{top50_df['price_change_percentage_24h'].unique()}')

print("-------------------------------------------------")

print(f'Pótolt érték és előző sor ellenőrzése: \n'
    f'{top50_df['price_change_percentage_24h'].iloc[[48,49]]}')

print("-------------------------------------------------")

#újra rendezem és indexálom
top50_df = top50_df.sort_values('price_change_percentage_24h', ascending = False).reset_index(drop=True)

#change_direction oszlop feltöltése:
top50_df['change_direction'] = top50_df['price_change_percentage_24h'].apply(direction)

print(f'Oszlopok ellenőrzése \n'
      f'{top50_df.columns}')
print("-------------------------------------------------")

print(f'Végző ellenőrzés ránézésre: \n'
    f'{top50_df[['id', 'symbol', 'name', 'price_change_percentage_24h','change_direction']].head()} \n'
    f'------------------------------------------------- \n'
    f'{top50_df[['id', 'symbol', 'name', 'price_change_percentage_24h', 'change_direction']].tail()}')