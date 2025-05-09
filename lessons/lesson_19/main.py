from auchan_scraper import AuchanScraper
import os
import time


def main():
    scraper = AuchanScraper()
    URLS_FILE_PATH = "lessons/lesson_19/all_auchan_urls.txt"
    SCRAPED_DATA_PATH = "lessons/lesson_19/auchan_all_products.csv"

    if os.path.exists(URLS_FILE_PATH):
        print("URL list already exists, reading from file..")
        urls = scraper.read_urls_from_file(URLS_FILE_PATH)
    else:
        print("No URL list yet, reading from sitemap")
        urls = scraper.get_urls_from_sitemap("https://auchan.hu/products-sitemap.xml")
        scraper.write_urls_to_file(urls, URLS_FILE_PATH)

    print(urls[:10])
    scraper.initialize_webdriver()

    data = []
    for url in urls[:50]:
        product_data = scraper.scrape_product_data(url)
        data.append(product_data)
    
    scraper.load_results_to_csv(data=data,filepath=SCRAPED_DATA_PATH)
    print("Successfully scraped Auchan data.")

if __name__ == "__main__":
    main()