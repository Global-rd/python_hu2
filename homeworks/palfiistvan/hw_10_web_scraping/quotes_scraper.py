from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import quotes_selectors as sel


class QuotesScraper:

    def __init__(self):
        options = Options()
        options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=options)
        self.wait = WebDriverWait(self.driver, 10)

    def get_top_tags(self, url="https://quotes.toscrape.com/"):
        self.driver.get(url)
        tag_elements = self.driver.find_elements(By.CSS_SELECTOR, sel.get_tag_items_selector())
        return [tag.text for tag in tag_elements[:10]]

    def get_quotes_for_tag(self, tag):
        base_url = f"https://quotes.toscrape.com/tag/{tag}/"
        quotes = []
        page = 1
        while True:
            self.driver.get(f"{base_url}page/{page}/")
            try:
                quote_elements = self.wait.until(
                    EC.presence_of_all_elements_located((By.CLASS_NAME, sel.get_quote_block_class()))
                )
            except:
                break

            for quote_el in quote_elements:
                text = quote_el.find_element(By.CLASS_NAME, sel.get_quote_text_class()).text.strip()
                author = quote_el.find_element(By.CLASS_NAME, sel.get_quote_author_class()).text.strip()
                quotes.append({
                    "tag": tag,
                    "author": author,
                    "quote": text
                })

            next_button = self.driver.find_elements(By.CLASS_NAME, sel.get_next_button_class())
            if not next_button:
                break
            page += 1

        return quotes

    def scrape(self):
        all_quotes = []
        top_tags = self.get_top_tags()
        for tag in top_tags:
            print(f"Scraping quotes for tag: {tag}")
            tag_quotes = self.get_quotes_for_tag(tag)
            all_quotes.extend(tag_quotes)
        return all_quotes

    def close(self):
        self.driver.quit()

    @staticmethod
    def save_to_csv(quotes, filename="quotes.csv"):
        df = pd.DataFrame(quotes)
        df.to_csv(filename, index=False)