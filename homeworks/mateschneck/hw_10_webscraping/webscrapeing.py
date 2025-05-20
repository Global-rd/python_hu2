from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd

# Selenium
options = Options()
options.add_argument('--headless')  
driver = webdriver.Chrome(service=Service(), options=options)

BASE_URL = "https://quotes.toscrape.com"

#top10
driver.get(BASE_URL)
top_tags = driver.find_elements(By.CSS_SELECTOR, '.tag-item a')[:10]
top_tag_names = [tag.text for tag in top_tags]

#Minden tag idézeteinek gyűjtése
results = []

for tag in top_tag_names:
    print(f"Scraping tag: {tag}")
    page = 1
    while True:
        url = f"{BASE_URL}/tag/{tag}/page/{page}/"
        driver.get(url)
        time.sleep(1)

        quotes = driver.find_elements(By.CLASS_NAME, "quote")
        if not quotes:
            break

        for quote in quotes:
            text = quote.find_element(By.CLASS_NAME, "text").text
            author = quote.find_element(By.CLASS_NAME, "author").text
            results.append({
                "tag": tag,
                "author": author,
                "quote": text
            })
        page += 1

#CSV mentés
df = pd.DataFrame(results)
df.to_csv("quotes_by_tag.csv", index=False, encoding="utf-8")
print("Kész: quotes_by_tag.csv")

driver.quit()