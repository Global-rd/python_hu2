# XPath-ek és URL-ek a scrapinghez

# Alap URL
BASE_URL = "https://quotes.toscrape.com"

# TOP10 tagek XPath-ja
TOP10_TAG_XPATH = '/html/body/div[1]/div[2]/div[2]/span[{index}]/a'

# Pagination XPath
NEXT_BUTTON_XPATH = '/html/body/div[1]/div[2]/div[1]/nav/ul/li/a'

# A div-ek XPath-ja, amiben a quote és author található
QUOTE_DIV_XPATH = '/html/body/div[1]/div[2]/div[1]/div'

# CSV fájl elérési útvonal
CSV_FILE_PATH = "quote_scraper.csv"