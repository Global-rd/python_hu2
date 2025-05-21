import requests
import xml.etree.ElementTree as ET
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
import pandas as pd

import quot_selectors as qtags

class QuotScraper:

    def __init__(self):
        options = Options()
        options.add_argument("--headless")  # nem nyit böngészőablakot
        self.driver = webdriver.Chrome(options=options)

    def get_tag_urls(self, quotes_url):
        self.driver.get(quotes_url)

        try:
            # Várjuk meg, míg a tag-ek betöltődnek
            WebDriverWait(self.driver, 2).until(
                EC.presence_of_all_elements_located((By.XPATH, qtags.get_top10_tag_div()))
            )

            tag_elements = self.driver.find_elements(By.XPATH, qtags.get_tag_item())

            tag_urls = []
            for tag in tag_elements[:10]:  # csak a top 10-et kérjük le
                href = tag.get_attribute('href')
                if href:
                    tag_urls.append(href)

            print(f"Total tag URLs found: {len(tag_urls)}")
            return tag_urls

        except Exception as e:
            print(f"Hiba történt: {e}")
            return []

    def get_quotes_by_tag_url(self, tag_url):
        self.driver.get(tag_url)
        quotes_data = []
        
        tag = tag_url.rstrip('/').split('/')[-1]

        while True:
            try:
                WebDriverWait(self.driver, 5).until(
                    EC.presence_of_all_elements_located((By.XPATH, qtags.get_quote_xpath()))
                )

                quote_blocks = self.driver.find_elements(By.CLASS_NAME, "quote")

                for block in quote_blocks:
                    text = block.find_element(By.CLASS_NAME, "text").text.strip()
                    author = block.find_element(By.CLASS_NAME, "author").text.strip()

                    quotes_data.append({
                        "quote": text,
                        "author": author,
                        "tag": tag
                    })

                # Lapozás, ha van
                next_button = self.driver.find_elements(By.XPATH, '//li[@class="next"]/a')
                if next_button:
                    next_button[0].click()
                    WebDriverWait(self.driver, 5).until(
                        EC.presence_of_all_elements_located((By.XPATH, qtags.get_quote_xpath()))
                    )
                else:
                    break

            except Exception as e:
                print(f"Hiba történt az idézetek lekérésekor: {e}")
                break

        return quotes_data

    def quit(self):
        self.driver.quit()