# scraper.py

import csv
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selector import BASE_URL, TOP10_TAG_XPATH, NEXT_BUTTON_XPATH, QUOTE_DIV_XPATH, CSV_FILE_PATH

#------TOP10 tag kinyeréselistába--------------------------------------------------

def get_top10_tags_from_class_xpath(driver) -> list:
    tags = []

    for i in range(1, 11):  # Loopolunk 1-től 10-ig
        xpath = TOP10_TAG_XPATH.format(index=i)  # Itt használjuk a TOP10_TAG_XPATH-t a config-ból
        try:
            tag_element = driver.find_element(By.XPATH, xpath)
            tags.append(tag_element.text)  # Hozzáadjuk a szöveget a listához
        except Exception as e:
            print(f"Hiba történt az {i}. tag kinyerésekor: {e}")

    return tags

#------------------------------------------------------------------------------------

#----- ezekkel a tagekkel már ki tudjuk nyerni a quote és author adatokat-------------

# a tag url-ek alatt lévő div-ek egyben tartalmazzák a quote és author párokat, ezeket lekérjük, ügyelünk a pagination-re is
def get_quotes_and_authors_for_tag(driver, tag_url):
    quotes = []
    authors = []
    
    while True:
        # a tag url-jére navigálunk
        driver.get(tag_url)

        # várakozás az adatok betöltésére
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, '//div[@class="quote"]'))
        )

        # az oldalról leolvasás
        div_elements = driver.find_elements(By.XPATH, QUOTE_DIV_XPATH)  # Itt használjuk a QUOTE_DIV_XPATH-t a config-ból
        
        for div in div_elements:
            try:
                # a divek leolvasása egyesével
                quote = div.find_element(By.XPATH, './span[@class="text"]').text.strip()
                author = div.find_element(By.XPATH, './span/small').text.strip()
                quotes.append(quote)
                authors.append(author)
            except Exception as e:
                print(f"Hiba történt a quote vagy author kinyerésekor: {e}")

        # pagination, "next" gomb 
        try:
            next_button = driver.find_element(By.XPATH, NEXT_BUTTON_XPATH)  # Itt használjuk a NEXT_BUTTON_XPATH-t a config-ból
            if "next" in next_button.get_attribute("class"): 
                next_button.click()  # ha van, akkor átlépünk a kövektező oldalra
            else:
                break 
        except NoSuchElementException:
            break 

    return quotes, authors

# a quote-ok és a hozzájuk tartozó author-ok mentése a csv-be
def save_quotes_and_authors_to_csv(driver, tags, filename=CSV_FILE_PATH):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['quote', 'author', 'tag'])  # oszlopok megadása

        for tag in tags:
            tag_url = f"{BASE_URL}/tag/{tag.lower()}/"  # Az alap URL a config-ból
            print(f"Processing tag: {tag}")

            quotes, authors = get_quotes_and_authors_for_tag(driver, tag_url)

            # kapcsola megadása hogy a megfelelő helyre kerüljenek a csv-ben
            for quote, author in zip(quotes, authors):
                writer.writerow([quote, author, tag])
