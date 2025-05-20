"""
Main script for the quotes scraper.
This script orchestrates the scraping process and saves the results to a CSV file.
"""

import pandas as pd
from quote_scraper import setup_driver, get_top_tags, get_quotes_for_tag


def main():
    """
    Main function to run the quotes scraper.
    """
    # Setup
    base_url = "https://quotes.toscrape.com/"
    driver = setup_driver(headless=True)

    try:
        # Get the top 10 tags
        print("Getting top 10 tags...")
        top_tags = get_top_tags(driver, base_url, num_tags=10)

        # Initialize an empty list to store all quotes
        all_quotes = []

        # Scrape quotes for each tag
        for tag in top_tags:
            print(f"\nScraping quotes for tag: {tag}")
            tag_quotes = get_quotes_for_tag(driver, base_url, tag)
            all_quotes.extend(tag_quotes)

        # Convert to DataFrame
        print("\nCreating DataFrame...")
        quotes_df = pd.DataFrame(all_quotes)

        # Save to CSV
        output_file = "quotes_by_tag.csv"
        quotes_df.to_csv(output_file, index=False)
        print(f"\nSaved {len(quotes_df)} quotes to {output_file}")

        # Print summary
        print("\nSummary by tag:")
        tag_counts = quotes_df["tag"].value_counts()
        for tag, count in tag_counts.items():
            print(f"- {tag}: {count} quotes")

    finally:
        driver.quit()


if __name__ == "__main__":
    main()
