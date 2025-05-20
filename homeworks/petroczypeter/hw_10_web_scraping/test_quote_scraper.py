"""
Test module for the quote scraper.
Tests the selectors and basic functionality of the scraper.
"""

import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Import our selectors
from quote_selector import (
    TOP_TAGS_SELECTOR,
    QUOTE_SELECTOR,
    QUOTE_TEXT_SELECTOR,
    QUOTE_AUTHOR_SELECTOR,
    QUOTE_TAGS_SELECTOR,
    NEXT_PAGE_SELECTOR,
)


class QuotesScraperTest(unittest.TestCase):
    """Test class for the quotes scraper."""

    def setUp(self):
        """Set up the webdriver before each test."""
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Run in headless mode
        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()), options=chrome_options
        )
        self.base_url = "https://quotes.toscrape.com/"

    def tearDown(self):
        """Clean up after each test."""
        self.driver.quit()

    def test_top_tags_selector(self):
        """Test that the top tags selector works."""
        self.driver.get(self.base_url)
        tags = self.driver.find_elements(By.CSS_SELECTOR, TOP_TAGS_SELECTOR)
        self.assertTrue(len(tags) > 0, "No tags found on the homepage")
        print(f"Found {len(tags)} tags on the homepage")

    def test_quote_selectors(self):
        """Test that the quote selectors work."""
        self.driver.get(self.base_url)
        quotes = self.driver.find_elements(By.CSS_SELECTOR, QUOTE_SELECTOR)
        self.assertTrue(len(quotes) > 0, "No quotes found on the homepage")

        # Test the first quote
        first_quote = quotes[0]
        text = first_quote.find_element(By.CSS_SELECTOR, QUOTE_TEXT_SELECTOR).text
        author = first_quote.find_element(By.CSS_SELECTOR, QUOTE_AUTHOR_SELECTOR).text
        tags = first_quote.find_elements(By.CSS_SELECTOR, QUOTE_TAGS_SELECTOR)

        self.assertTrue(len(text) > 0, "Quote text is empty")
        self.assertTrue(len(author) > 0, "Author name is empty")
        self.assertTrue(len(tags) > 0, "No tags found for the quote")

        print(f"First quote: '{text[:30]}...' by {author}")

    def test_pagination_selector(self):
        """Test that the pagination selector works."""
        self.driver.get(self.base_url)
        next_buttons = self.driver.find_elements(By.CSS_SELECTOR, NEXT_PAGE_SELECTOR)
        self.assertTrue(len(next_buttons) > 0, "No 'Next' button found on the homepage")


if __name__ == "__main__":
    unittest.main()
