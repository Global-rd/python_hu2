import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Böngésző beállítása
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
wait = WebDriverWait(driver, 10)

def fetch_top_10_tags():
    driver.get("https://quotes.toscrape.com/")
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'tag-item')))
    tag_elements = driver.find_elements(By.CLASS_NAME, 'tag-item')
    return [elem.text for elem in tag_elements[:10]]

def fetch_quotes_by_tag(tag_name):
    quotes_data = []
    base_url = f"https://quotes.toscrape.com/tag/{tag_name}/"
    driver.get(base_url)

    while True:
        wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'quote')))
        quotes_on_page = driver.find_elements(By.CLASS_NAME, 'quote')

        for quote in quotes_on_page:
            text = quote.find_element(By.CLASS_NAME, 'text').text
            author = quote.find_element(By.CLASS_NAME, 'author').text
            quotes_data.append({
                "tag": tag_name,
                "author": author,
                "quote": text
            })

        # Ellenőrizd, van-e következő oldal
        try:
            next_link = driver.find_element(By.CSS_SELECTOR, "li.next a")
            next_link.click()
        except:
            break

    return quotes_data

def main():
    all_quotes = []
    popular_tags = fetch_top_10_tags()

    for tag in popular_tags:
        print(f"Letöltés: {tag}")
        tag_quotes = fetch_quotes_by_tag(tag)
        all_quotes.extend(tag_quotes)

    df = pd.DataFrame(all_quotes)
    df.to_csv("quotes.csv", index=False, encoding="utf-8")
    print("Mentés kész: quotes.csv")

if __name__ == "__main__":
    main()
    driver.quit()
