from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from pathlib import Path
import pandas as pd

import toscrape_scraper

def write_to_csv_file(quotes: list, authors: list, tags: list):

    location = Path.cwd() / "quotes.csv"

    dataframe = pd.DataFrame({'quote': quotes, 'author': authors, 'tag': tags})

    dataframe.to_csv(location, index=False)


def main():

    driver = webdriver.Chrome(options=Options())

    top_10_tags = toscrape_scraper.scrape_top10_tags(driver)
    authors, quotes, tags = toscrape_scraper.scrape_authors_quotes_tags(driver, top_10_tags)

    write_to_csv_file(authors, quotes, tags)

    driver.quit()

if __name__ == "__main__":

    main()