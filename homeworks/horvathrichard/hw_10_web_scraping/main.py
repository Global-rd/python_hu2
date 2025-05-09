# main.py

import os
from selenium import webdriver
from scraper import get_top10_tags_from_class_xpath, save_quotes_and_authors_to_csv
from selector import CSV_FILE_PATH

if __name__ == '__main__':
    # webdriver
    driver = webdriver.Chrome()

    # TOP10 tag
    driver.get("https://quotes.toscrape.com")  # Kezdő URL

    tags = get_top10_tags_from_class_xpath(driver)  # Top10 tag kinyerése

    # quote-ok és az author-ok mentése a csv-be
    save_quotes_and_authors_to_csv(driver, tags)

    # a böngésző bezárása
    driver.quit()

    # a fájl abszolút elérési útvonalának kiírása
    csv_path = os.path.abspath(CSV_FILE_PATH)
    print(f"Data successfully saved to: {csv_path}") # kell az útvonal is miután elment fél óra azzal is, miért nem dolgozik a másik mappában létrehozott csv-be :')
