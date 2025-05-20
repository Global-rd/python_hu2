"""
This module contains the functionality to scrape quotes from quotes.toscrape.com site.
It provides functions to extract the top tags and quotes for each tag.
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
import time

# Import our selectors
from quote_selector import (
    TOP_TAGS_SELECTOR,
    QUOTE_SELECTOR,
    QUOTE_TEXT_SELECTOR,
    QUOTE_AUTHOR_SELECTOR,
    NEXT_PAGE_SELECTOR,
)


def setup_driver(headless=True):
    """
    Set up and return a configured Chrome WebDriver.

    Args:
        headless (bool): Whether to run Chrome in headless mode

    Returns:
        WebDriver: Configured Chrome WebDriver
    """
    chrome_options = Options()
    if headless:
        chrome_options.add_argument("--headless")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()), options=chrome_options
    )
    return driver


def get_top_tags(driver, base_url, num_tags=10):
    """
    Get the top tags from the homepage.

    Args:
        driver (WebDriver): Selenium WebDriver
        base_url (str): Base URL of the website
        num_tags (int): Number of top tags to return

    Returns:
        list: List of top tag names
    """
    driver.get(base_url)
    tag_elements = driver.find_elements(By.CSS_SELECTOR, TOP_TAGS_SELECTOR)

    # Extract tag names and limit to the specified number
    tags = [tag.text for tag in tag_elements[:num_tags]]
    print(f"Found top {len(tags)} tags: {tags}")
    return tags


def get_quotes_for_tag(driver, base_url, tag):
    """
    Get all quotes for a specific tag, handling pagination.

    Args:
        driver (WebDriver): Selenium WebDriver
        base_url (str): Base URL of the website
        tag (str): Tag name to scrape quotes for

    Returns:
        list: List of dictionaries containing quote data
    """
    # Construct the URL for the tag page
    tag_url = f"{base_url}tag/{tag}/"
    driver.get(tag_url)

    quotes_data = []
    page_num = 1

    while True:
        print(f"Scraping page {page_num} for tag '{tag}'...")

        # Find all quote elements on the current page
        quote_elements = driver.find_elements(By.CSS_SELECTOR, QUOTE_SELECTOR)

        # Extract data from each quote
        for quote_element in quote_elements:
            quote_text = quote_element.find_element(
                By.CSS_SELECTOR, QUOTE_TEXT_SELECTOR
            ).text
            # Remove the quotation marks from the beginning and end
            quote_text = quote_text[1:-1]

            author = quote_element.find_element(
                By.CSS_SELECTOR, QUOTE_AUTHOR_SELECTOR
            ).text

            quotes_data.append({"tag": tag, "author": author, "quote": quote_text})

        # Check if there's a next page
        try:
            next_button = driver.find_element(By.CSS_SELECTOR, NEXT_PAGE_SELECTOR)
            next_button.click()
            page_num += 1
            # Add a small delay to prevent overwhelming the server
            time.sleep(1)
        except NoSuchElementException:
            # No more pages
            break

    print(f"Found {len(quotes_data)} quotes for tag '{tag}'")
    return quotes_data
