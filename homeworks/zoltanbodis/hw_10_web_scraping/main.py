from quot_scraper import QuotScraper
import pandas as pd
import os

if __name__ == "__main__":
   
   scraper = QuotScraper()

   try:
      tag_urls = scraper.get_tag_urls("https://quotes.toscrape.com")

      all_quotes = []
      
      for tag_url in tag_urls:
         print(f"Gyűjtés folyamatban: {tag_url}")
         quotes = scraper.get_quotes_by_tag_url(tag_url)
         all_quotes.extend(quotes)

      df = pd.DataFrame(all_quotes)
      df.to_csv("all_quotes.csv", index=False)
      print(f"all_quotes.csv sikeresen elmentve: {os.getcwd()}")

   finally:
        scraper.quit()