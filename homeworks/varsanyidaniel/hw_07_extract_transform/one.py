import requests
import pandas as pd

url = "https://api.coingecko.com/api/v3/coins/markets"
parameters = {
    "vs_currency" : "usd",
    "per_page" : 250,
}

response = requests.get(url, params=parameters)

if response.status_code == 200:

    data = response.json()
    df = pd.DataFrame(data)

    print("Empty cells per each column:")
    print(df.
          isna().
          sum())
    
    print(f"\nThe SUM of all market caps: {df["market_cap"].sum()}\n")

    top50_df = df.sort_values(by="current_price", ascending=False).head(50)
    top50_df = top50_df.sort_values(by="price_change_percentage_24h", ascending=False)

    def determine_direction(direction):
        if direction > 0:
            return "+"
        elif direction == 0:
            return "0"
        else:
            return "-"
    top50_df["change_direction"] = top50_df["price_change_percentage_24h"].apply(determine_direction)

    print("Final result of the top50_df DataFrame:\n", top50_df.reset_index())


else:
    print("Something went wrong...")