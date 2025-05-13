import os
from selenium import webdriver

from toscrape_scraper import get_top10_tag_links, save_quotes_to_csv
from toscrape_selectors import CSV_FILE_PATH

def get_next_available_filename(base_path):
    base, ext = os.path.splitext(base_path)
    i = 1
    while True:
        new_path = f"{base}_{i}{ext}"
        if not os.path.exists(new_path):
            return new_path
        i += 1

if __name__ == '__main__':
    driver = webdriver.Chrome()
    tag_links = get_top10_tag_links(driver)
    print([tag for tag, _ in tag_links])
    csv_path = get_next_available_filename(CSV_FILE_PATH)
    save_quotes_to_csv(driver, tag_links, filename=csv_path)
    driver.quit()
    abs_csv_path = os.path.abspath(csv_path)
    print(f"Data successfully saved to: {abs_csv_path}")