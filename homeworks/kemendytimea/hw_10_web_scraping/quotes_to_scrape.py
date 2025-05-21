import os
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

script_dir = os.path.dirname(os.path.realpath(__file__))
csv_file_path = os.path.join(script_dir, 'quotes_to_scrape.csv')

if os.path.exists(csv_file_path):
    os.remove(csv_file_path)

driver = webdriver.Chrome()

wait = WebDriverWait(driver, 10)

driver.get("https://quotes.toscrape.com/")

tags = []
tag_elements = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'tag-item')))
for tag in tag_elements:
    tags.append(tag.text)

print("Top 10 tag:", tags)
data = []

for tag in tags:
    driver.get(f"https://quotes.toscrape.com/tag/{tag.replace(' ', '-')}/")
    time.sleep(2)

    while True:
        quotes = driver.find_elements(By.CLASS_NAME, 'quote')
        
        for quote in quotes:
            text = quote.find_element(By.CLASS_NAME, 'text').text
            author = quote.find_element(By.CLASS_NAME, 'author').text
            data.append([tag, author, text])
        
        try:
            next_button = driver.find_element(By.CLASS_NAME, 'next')
            next_button.click()
            time.sleep(2)
        except:
            break

df = pd.DataFrame(data, columns=['tag', 'author', 'quote'])
df.to_csv(csv_file_path, index=False)

driver.quit()