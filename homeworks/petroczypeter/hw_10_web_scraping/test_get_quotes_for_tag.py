"""
Test script for the get_quotes_for_tag function.
"""

from quote_scraper import setup_driver, get_quotes_for_tag


def test_get_quotes_for_tag():
    """Test the get_quotes_for_tag function with a single tag."""
    driver = setup_driver(headless=True)
    base_url = "https://quotes.toscrape.com/"

    # Choose a tag to test with
    test_tag = "love"

    try:
        # Get quotes for the test tag
        quotes = get_quotes_for_tag(driver, base_url, test_tag)

        # Print summary
        print(f"Successfully retrieved {len(quotes)} quotes for tag '{test_tag}'")

        # Print a few examples
        print("\nExample quotes:")
        for i, quote_data in enumerate(
            quotes[:3], 1
        ):  # Print first 3 quotes as examples
            print(f"\nExample {i}:")
            print(f"Tag: {quote_data['tag']}")
            print(f"Author: {quote_data['author']}")
            print(f"Quote: \"{quote_data['quote']}\"")

        # Verify we got some quotes
        assert (
            len(quotes) > 0
        ), f"Expected to find quotes for tag '{test_tag}', but found none"

        # Verify the structure of the data
        for quote_data in quotes:
            assert "tag" in quote_data, "Missing 'tag' field in quote data"
            assert "author" in quote_data, "Missing 'author' field in quote data"
            assert "quote" in quote_data, "Missing 'quote' field in quote data"
            assert (
                quote_data["tag"] == test_tag
            ), f"Expected tag '{test_tag}', got '{quote_data['tag']}'"

        print("\nTest passed!")

    finally:
        driver.quit()


if __name__ == "__main__":
    test_get_quotes_for_tag()
