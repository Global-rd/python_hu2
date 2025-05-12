from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

driver = webdriver.Chrome()
driver.get("https://quotes.toscrape.com/")

tag_elements = driver.find_elements(By.CSS_SELECTOR, ".tag-item a")
top_10_tags = [tag.text for tag in tag_elements[:10]]

quotes_list = []

for tag in top_10_tags:
    driver.get(f"https://quotes.toscrape.com/tag/{tag}/")
    print(f"{tag}")

    while True:
        quotes = driver.find_elements(By.CLASS_NAME, "quote")

        for quote in quotes:
            text = quote.find_element(By.CLASS_NAME, "text").text
            author = quote.find_element(By.CLASS_NAME, "author").text

            quotes_list.append({
                "tag": tag,
                "author": author,
                "quote": text})

        try:
            next_button = driver.find_element(By.CSS_SELECTOR, ".next a")
            next_button.click()
            time.sleep(1)  
        except:
            break 



df = pd.DataFrame(quotes_list)
df.to_csv("top10_tag_quotes.csv", index=False, encoding="utf-8")
print("Saved to CSV file.")

driver.quit()

