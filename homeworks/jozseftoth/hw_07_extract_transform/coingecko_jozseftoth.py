import requests
import pandas as pd

# 250 highest market cap cryptocurrency adatok lekérdezése a CoinGecko API-ból
url = "https://api.coingecko.com/api/v3/coins/markets"
params = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 250,
    "page": 1
}
response = requests.get(url, params=params)
data = response.json()

# dataframe
df = pd.DataFrame(data)

# 1. Determine the number of empty cells in each column of the dataframe and print
missing_values = df.isnull().sum()
print("Missing values per column:\n", missing_values)

# 2. Determine the market_cap for the whole dataframe and print
total_market_cap = df['market_cap'].sum()
print("Total market cap:", total_market_cap)

# 3. Create a new dataframe called top50_df, where only the top 50 cryptocurrencies are stored based on current_price
top50_df = df.nlargest(50, 'current_price')

# 4. Sort the top50_df in descending order based on price_change_percentage_24h
top50_df = top50_df.sort_values(by='price_change_percentage_24h', ascending=False)

# 5. Create a new column in top50_df called change_direction
top50_df['change_direction'] = top50_df['price_change_percentage_24h'].apply(lambda x: '+' if x > 0 else '-' if x < 0 else '0')

# dataframe print (top50_df)
print(top50_df)
