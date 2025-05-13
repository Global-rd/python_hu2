import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# WebDriver inicializálása
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Funkció a top 10 tag lekérésére
def get_top_tags():
    driver.get("https://quotes.toscrape.com/")
    time.sleep(2)
    
    tags  = driver.find_elements(By.CLASS_NAME, 'tag-item')
    # Csak az első 10 tag szövegének kinyerése
    toptags = [tag.text for tag in tags[:10]]


    return toptags

# Funkció, amely a tag-ek idézeteit lekéri
def get_quotes_for_tag(tag):
    quotes = []
    driver.get(f"https://quotes.toscrape.com/tag/{tag}/")
    time.sleep(2)
    
    while True:
        # Idézetek összegyűjtése az aktuális oldalon
        quote_elements = driver.find_elements(By.CSS_SELECTOR, "div.quote")
        
        for quote_elem in quote_elements:
            author = quote_elem.find_element(By.CSS_SELECTOR, "span small").text
            quote_text = quote_elem.find_element(By.CSS_SELECTOR, "span.text").text
            quotes.append({"tag": tag, "author": author, "quote": quote_text})
        
        # Lapozás ellenőrzése
        try:
            next_button = driver.find_element(By.CSS_SELECTOR, 'li.next a')
            next_button.click()
            time.sleep(2)
        except:
            break
    
    return quotes

# A fő funkció a top 10 tag idézeteinek összegyűjtésére
def scrape_quotes():
    top_tags = get_top_tags()
    all_quotes = []
    
    for tag in top_tags:
        print(f"Scraping quotes for tag: {tag}")
        quotes = get_quotes_for_tag(tag)
        all_quotes.extend(quotes)
    
    # Adatok mentése CSV fájlba
    df = pd.DataFrame(all_quotes)
    df.to_csv("quotes.csv", index=False, encoding='utf-8')
    print("Scraping complete. Data saved to quotes.csv.")

# Indítjuk el a scrape folyamatot
scrape_quotes()

# WebDriver bezárása
driver.quit()