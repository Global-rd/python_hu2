from quotes_scraper import QuotesScraper


def main():
    scraper = QuotesScraper()
    try:
        quotes = scraper.scrape()
        scraper.save_to_csv(quotes, "quotes.csv")
        print("Scraping completed successfully. Data saved to 'quotes.csv'.")
    finally:
        scraper.close()


if __name__ == "__main__":
    main()