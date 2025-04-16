import pandas as pd
import requests

url = "https://api.coingecko.com/api/v3/coins/markets"
params = {
    "vs_currency": "usd",  
    "per_page": 250,      
    "order": "market_cap_desc" 
}

response = requests.get(url, params=params)
data = response.json()
df = pd.DataFrame(data)

print("\nNumber of empty cells by columns:\n")
print(df.isnull().sum())
    
total_market_cap = df['market_cap'].sum()
print(f"\nTotal crypto market capitalization: ${total_market_cap:,.2f}\n")

top50_df = df.sort_values(by='current_price', ascending=False).head(50).copy()

top50_df.sort_values(by='price_change_percentage_24h', ascending=False, inplace=True)

def get_change_direction(change):
    if change > 0:
        direction = '\u2197'
    elif change < 0:
        direction = '\u2198'
    else:
        direction = '\u2192'
    return direction

top50_df['change_direction'] = top50_df['price_change_percentage_24h'].apply(get_change_direction)

print("Top 50 cryptos sorted by 24-hour exchange rate change:\n")
print(top50_df[['name', 'current_price', 'price_change_percentage_24h', 'change_direction']].head(50))

