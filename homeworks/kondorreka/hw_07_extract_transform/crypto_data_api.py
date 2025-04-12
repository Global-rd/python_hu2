"""A következő feladatban a coinGecko public API-járól kell majd adatokat kinyerned,
és ezeket elemezni Python segítségével.
A kövekező endpoint-ról “https://api.coingecko.com/api/v3/coins/markets” húzd le
a 250 legnagyobb market cap-pel rendelkező kriptovalutát (értelmezd az api
dokumentációt, két paramétert kell összesen használnod, és 1 api hívásból
megszerezhető az adat). *market cap = kibocsátott darabszám * ár
"""
import requests
def crypto_data():
    
    url = 'https://api.coingecko.com/api/v3/coins/markets'

    params = {"vs_currency": "usd", #string #required #target currency of coins and market data
            #"order": "market_cap_desc", #string #sort result by field, default: market_cap_desc
            "per_page": 250, #number #total results per page,default: 100 #Valid values: 1...250"
            "page" : 1 #number #page #through results, default: 1     
             }

    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers, params=params)

    if response.status_code ==200:
        return response.json()
    else: 
        raise Exception(f"Hiba a lekérdezés során. Hibakód: {response.status_code}.  Hibaüzenet: {response.text}")
        