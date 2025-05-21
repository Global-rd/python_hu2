"""
Test script for the get_top_tags funciton.
"""

from quote_scraper import setup_driver, get_top_tags


def test_get_top_tags():
    """Test the get_top_tags function."""
    driver = setup_driver(headless=True)
    base_url = "https://quotes.toscrape.com/"

    try:
        # Get the top 10 tags
        tags = get_top_tags(driver, base_url, num_tags=10)

        # Print the results
        print(f"Successfully retrieved {len(tags)} tags:")
        for i, tag in enumerate(tags, 1):
            print(f"{i}. {tag}")

        # Verify we got the expected number of tags
        assert len(tags) == 10, f"Expected 10 tags, but got {len(tags)}"

        print("Test passed!")

    finally:
        driver.quit()


if __name__ == "__main__":
    test_get_top_tags()
