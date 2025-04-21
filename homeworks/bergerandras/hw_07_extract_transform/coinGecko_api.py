import requests
import pandas

url = "https://api.coingecko.com/api/v3/coins/markets"
parameters = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 250,
    "page": 1
}

response = requests.get(url, params=parameters)

if response.status_code == 200:

    data = response.json()
    data_frames = pandas.DataFrame(data)

    print("Empty cells:")
    print(data_frames.isnull().sum())

    total_market_cap = data_frames["market_cap"].sum()
    print(f"\nTotal market cap amount: {total_market_cap:,}")

    top50_df = data_frames.sort_values(by="current_price", ascending=False).head(50)

    top50_df = top50_df.sort_values(by="price_change_percentage_24h", ascending=False)

    def get_change_direction(pct):
        if pct > 0:
            return "+"
        elif pct < 0:
            return "-"
        else:
            return "0"

    top50_df["change_direction"] = top50_df["price_change_percentage_24h"].apply(get_change_direction)

    print("\nTop 50 coins:")
    print(top50_df[["id", "current_price", "price_change_percentage_24h", "change_direction"]])

elif response.status_code == 404:

    print("Requested data not found!")

else:

    print("An error accured while trying to get data.")