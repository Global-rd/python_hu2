from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

import toscrape_selectors as TSS

def scrape_next_page(driver, quotes_list: list, authors_list: list, tags_list: list, tag, timeout=10):

    next_button = driver.find_element(by=By.XPATH, value=TSS.get_next_button_xpath())

    next_button.click()

    WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH, TSS.get_quotes_div_xpath())))

    quotes_div = driver.find_elements(by=By.XPATH, value=TSS.get_quotes_div_xpath())

    for quote_div in quotes_div:
                    
        quote = quote_div.find_element(by=By.XPATH, value='./span[1]')
        author = quote_div.find_element(by=By.XPATH, value='./span[2]/small')

        quotes_list.append(quote.text.strip())
        authors_list.append(author.text.strip())
        tags_list.append(tag)

    try:

        scrape_next_page(driver, quotes_list, authors_list, tags_list, tag)

    except:

        return [quotes_list, authors_list, tags_list]

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

def scrape_authors_quotes_tags(driver, tags: list, timeout=10):

    quotes_list = []
    authors_list = []
    tags_list = []

    for tag in tags:

        driver.get(f"https://quotes.toscrape.com/tag/{tag}/")

        try:

            WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.XPATH, TSS.get_quotes_div_xpath())))

            quotes_div = driver.find_elements(by=By.XPATH, value=TSS.get_quotes_div_xpath())

            for quote_div in quotes_div:

                quote = quote_div.find_element(by=By.XPATH, value='./span[1]')
                author = quote_div.find_element(by=By.XPATH, value='./span[2]/small')

                quotes_list.append(quote.text.strip())
                authors_list.append(author.text.strip())
                tags_list.append(tag)

            try:
                
                quotes_list, authors_list, tags_list = scrape_next_page(driver, quotes_list, authors_list, tags_list, tag, timeout=10)

            except:

                pass

        except TimeoutException:

            print("Quotes did not load in time!")

            driver.quit()

    return [quotes_list, authors_list, tags_list]