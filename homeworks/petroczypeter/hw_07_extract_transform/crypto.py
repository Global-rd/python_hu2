import requests
import pandas as pd
import logging

# The 4 steps of logging setup:

# 1. Create handlers - where the logs will go
file_handler = logging.FileHandler("crypto_analysis.log")
stream_handler = logging.StreamHandler()

# 2. Define the formatter - how the logs will look
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

# 3. Assigning the formatter to each handler
file_handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)

# 4. Creating logger and assign the handlers to it
logger = logging.getLogger("crypto_analysis")
logger.setLevel(logging.INFO)
logger.addHandler(file_handler)
logger.addHandler(stream_handler)

# API endpoint
url = "https://api.coingecko.com/api/v3/coins/markets"

# Parameters
# vs_currency will be needed to specify the currency
# per_page will specify how many results do we need
params = {
    "vs_currency": "USD",  # our base currency
    "per_page": 250,  # top 250 crypto
}

# Make API request
logger.info("Starting cryptocurrency dark magic")
logger.info("Making an API request to CoinGecko")
response = requests.get(url, params=params)

# Check if request was OK
if response.status_code == 200:
    # Parse the JSON response
    crypto_data = response.json()
    logger.info(f"successfully fetched data for {len(crypto_data)} cryptocurrencies")

    # the homework said we need the top 250, but it also said that we should use 2 parameters...
    # there was a 3rd parameter that I liked and wanted to use: "order": "market_cap_desc" however that would've made my params 3...
    # based on my past experience working with interfaces... let's double-check if the data is indeed ordered by market cap
    if len(crypto_data) > 1:
        is_ordered = crypto_data[0].get("market_cap", 0) > crypto_data[-1].get(
            "market_cap", 0
        )
        logger.info(f"Data ordering check: {is_ordered}")

    # convert response to pd DataFrame
    logger.info(f"Created DataFrame with shape: {df.shape}")

    # Let's check the dataframe
    print("DataFrame information:")
    print(df.info())

    # print the first 5 rows to check the data
    print("First 5 rows of the DataFrame:")
    print(df.head())

else:
    error_msg = f"API request failed with status code: {response.status_code}"
    logger.error(error_msg)
    print(f"Error: {response.status_code}")
    print(response.text)

# count empty cells in each column
logger.info("Task-01: Count empty cells in each column")
empty_cells = df.isna().sum()
print("Task-01: Count empty cells in each column")
print(empty_cells)
empty_column_count = sum(1 for count in empty_cells if count > 0)
logger.info(f"Found {empty_column_count} columns with empty cells")

# Calculate total market cap
logger.info("Task-02: Calculating total market cap")
total_market_cap = df["market_cap"].sum()
print("Task-02: Total market cap")
print(f"Total market cap: ${total_market_cap:,.2f}")
logger.info("Total market cap calculation completed")

# Create a new DataFrame with the top 50 cryptocurrencies by current price
logger.info("Task-03: Creating top 50 cryptocurrencies by current price")
# Sort by current_price in desc
sorted_df = df.sort_values(by="current_price", ascending=False)
# Take the first 50 rows
top50_df = sorted_df.head(50)
logger.info(f"Created filtered DataFrame with shape: {top50_df.shape}")
print("Task-03: Top 50 cryptocurrencies by current price:")
print(f"Shape of top50_df: {top50_df.shape}")
print(top50_df[["id", "symbol", "name", "current_price"]].head())

# Sort the top50_df by price_change_percentage_24h in desc
logger.info("Task-04: Sorting filtered DataFrame by 24h price change percentage")
print("Task-04: top 50 cryptos sorted by 24h price change %")
top50_df = top50_df.sort_values(by="price_change_percentage_24h", ascending=False)
print(
    top50_df[
        ["id", "symbol", "name", "current_price", "price_change_percentage_24h"]
    ].head()
)
logger.info("Sorting completed")

# New column 'change direction' based on 24h price change %
logger.info("Task-05: Adding change_direction column")


# Determine change direction
def get_change_direction(change_percentage):
    if change_percentage > 0:
        return "+"
    elif change_percentage < 0:
        return "-"
    else:
        return "0"


# Apply the function to create the new column
top50_df["change_direction"] = top50_df["price_change_percentage_24h"].apply(
    get_change_direction
)
logger.info("Successfully added change_direction column")

# Print out the results
print("Task-05: change_direction column")
print(
    top50_df[
        [
            "id",
            "symbol",
            "current_price",
            "price_change_percentage_24h",
            "change_direction",
        ]
    ].head(10)
)

logger.info("Cryptocurrency dark magic completed successfully")
