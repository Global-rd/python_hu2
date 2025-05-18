from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
import quotes_selectors as qs


def get_all_quotes_in_one_page(driver, actual_link, one_tag_name):
    driver.get(f"{actual_link}")
    list_of_quotes_in_page = []
    all_quotes_in_one_page = driver.find_elements(By.CLASS_NAME, value=qs.get_one_quote_name())

    for quote in all_quotes_in_one_page:
        one_quote_text = quote.find_element(By.CLASS_NAME, "text").text
        one_author = quote.find_element(By.CLASS_NAME, "author").text
        list_of_quotes_in_page.append({
            "tag": one_tag_name,
            "author": one_author,
            "quote": one_quote_text
        })
    return list_of_quotes_in_page   


def main():
    
    BASE_URL = "https://quotes.toscrape.com/"

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    driver.get(BASE_URL)
    
    # Néha nem akart betölteni az oldal rendesen, ezért tettem bele ezt a try kezelést...
    try:
        top10_tags = driver.find_elements(By.CLASS_NAME, value=qs.get_top_10_tag_names())
   
    except Exception as e:
        print(f"Hiba történt a top 10 tagek keresése közben: {e}")
    
    name_of_top10_tags = [tag.text for tag in top10_tags]
       
    list_of_quotes = []

    for one_tag in name_of_top10_tags:
        link = f"{BASE_URL}/tag/{one_tag}/"
        list_of_quotes.extend(get_all_quotes_in_one_page(driver, link, one_tag))
        # Ha nem fért el minden egy oldalon, sajnos ezt csak később vettem észre
        try:
            driver.find_element(By.XPATH, value=qs.get_next_page_link())
            link = f"{link}page/2/"
            list_of_quotes.extend(get_all_quotes_in_one_page(driver, link, one_tag))
        except:
            pass

    df = pd.DataFrame(list_of_quotes)
    df.to_csv("list_of_quotes.csv", index=False, encoding="utf-8")

if __name__ == "__main__":
    main()  