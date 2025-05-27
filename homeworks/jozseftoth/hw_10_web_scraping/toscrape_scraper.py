import csv
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from toscrape_selectors import URL, TOP10_TAG_XPATH, NEXT_BUTTON_XPATH, QUOTE_DIV_XPATH, CSV_FILE_PATH

def get_top10_tag_links(driver):
    driver.get(URL)
    tag_links = []
    for i in range(1, 11):
        xpath = TOP10_TAG_XPATH.format(index=i)
        tag_element = driver.find_element(By.XPATH, xpath)
        tag_name = tag_element.text
        tag_url = tag_element.get_attribute("href")
        tag_links.append((tag_name, tag_url))
    return tag_links

def get_quotes_for_tag(driver, tag_url):
    quotes_data = []
    driver.get(tag_url)
    while True:
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, QUOTE_DIV_XPATH))
        )
        div_elements = driver.find_elements(By.XPATH, QUOTE_DIV_XPATH)
        for div in div_elements:
            try:
                quote = div.find_element(By.XPATH, './span[@class="text"]').text.strip()
                # Replace fancy quotes with standard quotes
                quote = quote.replace('“', '"').replace('”', '"')
                author = div.find_element(By.XPATH, './span/small').text.strip()
                quotes_data.append({"quote": quote, "author": author})
            except Exception as e:
                print(f"An error occurred while processing a quote: {e}")
        # Next button
        try:
            next_button = driver.find_element(By.XPATH, NEXT_BUTTON_XPATH)
            if "next" in next_button.get_attribute("class"):
                next_button.click()
            else:
                break
        except:
            break
    return quotes_data

def save_quotes_to_csv(driver, tag_links, filename=CSV_FILE_PATH):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['quote', 'author', 'tag'])
        writer.writeheader()
        for tag, url in tag_links:
            print(f"Processing tag: {tag}")
            for item in get_quotes_for_tag(driver, url):
                item['tag'] = tag
                writer.writerow(item)
