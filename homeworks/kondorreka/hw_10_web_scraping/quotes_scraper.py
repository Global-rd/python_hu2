import requests
import xml.etree.ElementTree as ET
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
import pandas as pd

import quotes_selectors as quot

class QuotesScraper:

    def get_urls_from_quotes(self):
        print("Top 10 tag URL-jeinek összeállítása...")
        base_url = "https://quotes.toscrape.com/tag/"
    
        tags = self.get_top_tags()  

        urls = [f"{base_url}{tag}/" for tag in tags]

        print(f"{len(urls)} URL készült.")
        print("Első néhány URL:", urls[:5])
        return urls
    
    #url-ek kiírása text fileba    
    @staticmethod
    def write_urls_to_file(urls, file_name):
        with open(file_name, "w") as file:
            for url in urls:
                file.write(url + "\n")
        print(f"URLs has been written to {file_name}")

    #url-ek olvasása
    @staticmethod
    def read_urls_from_file(file_name):
        urls = []
        with open(file_name, "r") as file:
            for line in file:
                url = line.strip()
                if url:
                    urls.append(url)
        return urls

          
    def initialize_webdriver(self): #böngésző létrehozása 
        options = Options()
        self.driver = webdriver.Chrome(options=options)

    #Főoldal betöltése és top 10 tag összegyűjtése
    def get_top_tags(self):
        self.driver.get("https://quotes.toscrape.com/")
        tag_names = self.driver.find_elements(by=By.XPATH, value=quot.get_top_tags_xpath())
        
        tags = [element.text for element in tag_names]
                
        print(tags)
        return tags
        
        
    # def get_quotes_by_tags(self, tags):
    #     quote_text = self.driver.find_element(by=By.XPATH, value=quot.get_quote_text_xpath())
    #     return quote_text.text


    def scrape_quotes_all_pages(self, url):
        

        print(f"Oldal betöltése: {url}")
        self.driver.get(url)
        
        WebDriverWait(self.driver, 10).until( #vár, hogy megjelenjenek az idézetblokkok
            EC.presence_of_all_elements_located((By.XPATH, quot.get_quotes_block_xpath()))
        )

        data = []

        #Összes idézetblokk keresése
        quote_blocks = self.driver.find_elements(By.XPATH, quot.get_quotes_block_xpath())

        for block in quote_blocks:
            quote_text = block.find_element(By.XPATH, './/span[1]').text
            quote_author = block.find_element(By.XPATH, './/span/small').text
            quote_tags = block.find_elements(By.XPATH, './/div/a')

            tags = []
            for i in quote_tags:
                tags.append(i.text)

            data.append({
                "tag": ", ".join(tags),
                "quote": quote_text,
                "author": quote_author
            })

        return data
    
 
    @staticmethod
    def load_results_to_csv(data, filepath):
        df = pd.DataFrame(data)
        df.to_csv(filepath, index=False)

