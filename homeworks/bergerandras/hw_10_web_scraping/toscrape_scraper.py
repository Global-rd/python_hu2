from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

import toscrape_selectors as TSS

def scrape_top10_tags(driver, timeout=10):

    tags = []

    driver.get("https://quotes.toscrape.com/")

    try:

        WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH, TSS.get_top_10_tags_div_xpath())))

        top_10_tags = driver.find_elements(by=By.XPATH, value=TSS.get_top_10_tags_items_xpath())

        for tag in top_10_tags:

            tags.append(tag.text)

        return list(tags)
    
    except TimeoutException:

        print("Top 10 tags did not load in time!")

        driver.quit()

def scrape_authors_quotes_tags(driver, tags: list):

    quotes_list = []
    authors_list = []
    tags_list = []

    for tag in tags:

        print(f"Scraping tag: {tag}")

        page = 1

        while True:

            driver.get(f"https://quotes.toscrape.com/tag/{tag}/page/{page}/")

            quotes_div = driver.find_elements(by=By.XPATH, value=TSS.get_quotes_div_xpath())

            if not quotes_div:

                break 

            for quote_div in quotes_div:

                try:
                    
                    quote = quote_div.find_element(by=By.XPATH, value=TSS.get_quote_xpath())
                    author = quote_div.find_element(by=By.XPATH, value=TSS.get_author_xpath())

                    quotes_list.append(quote.text.strip())
                    authors_list.append(author.text.strip())
                    tags_list.append(tag)

                except:

                    continue

            page += 1

    return [quotes_list, authors_list, tags_list]