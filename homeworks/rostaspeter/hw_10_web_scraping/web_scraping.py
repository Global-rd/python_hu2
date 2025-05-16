from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import csv

def get_top_10_tags(driver):
    driver.get("https://quotes.toscrape.com/")
    time.sleep(1)
    tags = driver.find_elements(By.CSS_SELECTOR, ".tag-item a")
    top_10 = [tag.text for tag in tags[:10]]
    return top_10

def get_quotes_for_tag(driver, tag):
    quotes = []
    page = 1
    while True:
        url = f"https://quotes.toscrape.com/tag/{tag}/page/{page}/"
        driver.get(url)
        time.sleep(1)
        quote_elements = driver.find_elements(By.CLASS_NAME, "quote")
        if not quote_elements:
            break
        for q in quote_elements:
            text = q.find_element(By.CLASS_NAME, "text").text
            author = q.find_element(By.CLASS_NAME, "author").text
            quotes.append({
                "tag": tag,
                "author": author,
                "quote": text
            })
        page += 1
    return quotes

def main():
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        print("TOP 10 TAG LOADIN...")
        top_10_tags = get_top_10_tags(driver)
        all_quotes = []

        for tag in top_10_tags:
            print(f"TAGS: {tag}")
            quotes = get_quotes_for_tag(driver, tag)
            all_quotes.extend(quotes)

        print("CSV WRITING...")
        with open("top_10_tags_quotes.csv", mode="w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["tag", "author", "quote"])
            writer.writeheader()
            writer.writerows(all_quotes)

        print("WRITING COMPLETED.")

    finally:
        driver.quit()

if __name__ == "__main__":
    main()