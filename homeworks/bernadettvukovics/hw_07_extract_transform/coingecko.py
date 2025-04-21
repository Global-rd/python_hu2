import pandas as pd
import requests

# API URL
url = "https://api.coingecko.com/api/v3/coins/markets"

# Paraméterek
params = {
    'vs_currency': 'usd',  # Az árakat USD-ban kérjük
    'order': 'market_cap_desc',  # A legnagyobb market cap először
    'perpage': 250,  # 250 rekord
    'page': 1  # Az első oldal
}

# API hívás
response = requests.get(url, params=params)

# Ha a kérés sikeres, akkor az adatokat pandas DataFrame-be helyezzük
if response.status_code == 200:
    data = response.json()
    df = pd.DataFrame(data)

    # Üres cellák száma az egyes oszlopokban
    print("Üres cellák száma:")
    print(df.isna().sum())

    # Market cap összeg
    market_cap_sum = df['market_cap'].sum()
    print(f'\nTotal Market Cap: {market_cap_sum}')

    # Top 50 kriptovaluta készítése és rendezzük a current_price alapján
    top50_df = df.head(50)
    top50_df = top50_df.sort_values('current_price', ascending=False)

    # Hozzáadjuk a change_direction oszlopot
    top50_df['change_direction'] = top50_df['price_change_percentage_24h'].apply(
        lambda x: '+' if x > 0 else ('-' if x < 0 else '0')
    )

    # Eredmények
    print(f'\nTop 50 Cryptocurrencies:')
    print(top50_df)

else:
    print("Hiba történt az API híváskor.")