from quotes_scraper import QuotesScraper
import os
import time
import pandas as pd


def main():
    scraper = QuotesScraper()
    URLS_FILE_PATH = "homeworks/kondorreka/hw_10_web_scraping/all_quotes_urls.txt"
    SCRAPED_DATA_PATH = "homeworks/kondorreka/hw_10_web_scraping/quotes_all_quotes.csv"

    if os.path.exists(URLS_FILE_PATH): #ha létezik a all_quotes_urls.txt
        print("URL list already exists, reading from file.")
        urls = scraper.read_urls_from_file(URLS_FILE_PATH)
    else:
        print("No URL list yet, reading from sitemap") #ha nem létezik all_quotes_urls.txta
        urls = scraper.get_urls_from_quotes()
        scraper.write_urls_to_file(urls, URLS_FILE_PATH)

    print(urls)
    scraper.initialize_webdriver()

    all_quotes = []
    for url in urls:
        quotes = scraper.scrape_quotes_all_pages(url)
        all_quotes.extend(quotes)
    
    scraper.load_results_to_csv(data=all_quotes,filepath=SCRAPED_DATA_PATH)
    print("Successfully scraped Quotes data.")

    top_tags = scraper.get_top_tags()
    
    top_tag_quotes = []

    for quote in all_quotes:
        if quote["tag"] in top_tags:
            top_tag_quotes.append(quote)


    df_top_tag_quotes = pd.DataFrame(top_tag_quotes)
    df_top_tag_quotes.to_csv("homeworks/kondorreka/hw_10_web_scraping/quotes_top_10_tags.csv", index=False)

    print("Top 10 taghez tartozó idézetek elmentve a quotes_top_10_tags.csv fájlba.")



if __name__ == "__main__":
    main()