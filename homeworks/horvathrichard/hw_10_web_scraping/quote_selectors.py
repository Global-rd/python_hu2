import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import os


#------TOP10 tag kinyeréselistába--------------------------------------------------

def get_top10_tags_from_class_xpath(driver) -> list:
    tags = []

    for i in range(1, 11):  # Loopolunk 1-től 10-ig
        xpath = f'/html/body/div[1]/div[2]/div[2]/span[{i}]/a'
        try:
            tag_element = driver.find_element(By.XPATH, xpath)
            tags.append(tag_element.text)  # Hozzáadjuk a szöveget a listához
        except Exception as e:
            print(f"Hiba történt az {i}. tag kinyerésekor: {e}")

    return tags
#------------------------------------------------------------------------------------

#----- ezekkel a tagekkel már ki tudjuk nyerni a uote és author adatokat-------------

# a tag url-ek alatt lévő div-ek egyben tartalmazzák a quot és author párokat, ezeket lekérjük, ügyelünk a pagination-re is
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
        div_elements = driver.find_elements(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div')
        
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
            next_button = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/nav/ul/li/a')
            if "next" in next_button.get_attribute("class"): 
                next_button.click()  # ha van, akkor átlépünk a kövektező oldalra
            else:
                break 
        except NoSuchElementException:
            break 

    return quotes, authors

# a quote-ok és a hozzájuk tartozó author-ok mentése a csv-be
def save_quotes_and_authors_to_csv(driver, tags, filename='quote_scraper.csv'):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['quote', 'author', 'tag'])  # oszlopok megadása

        for tag in tags:
            tag_url = f"https://quotes.toscrape.com/tag/{tag.lower()}/"
            print(f"Processing tag: {tag}")

            quotes, authors = get_quotes_and_authors_for_tag(driver, tag_url)

            # kapcsola megadása hogy a megfelelő helyre kerüljenek a csv-ben
            for quote, author in zip(quotes, authors):
                writer.writerow([quote, author, tag]) 

csv_path = os.path.abspath("quote_scraper.csv")

# MAIN
if __name__ == '__main__':
    # webdriver
    driver = webdriver.Chrome()
    driver.get("https://quotes.toscrape.com")

    # TOP10 tag
    tags = get_top10_tags_from_class_xpath(driver)

    # quote-ok és az author-ok mentése a csv-be
    save_quotes_and_authors_to_csv(driver, tags)

    # a böngésző bezárása
    driver.quit()

    print(f"Data successfully saved to 'quote_scraper.csv'to: {csv_path}.") # kell az útvonal is miután elment fél óra azzal is, miért nem dolgozik a másik mappában létrehozott csv-be :')