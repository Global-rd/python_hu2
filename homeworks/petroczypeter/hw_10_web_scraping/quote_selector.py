"""
This module will contain CSS selectors for the homework: quotes.toscrape.com website.
These selectors help locate elements on the webpage for data extraction.
"""

# Selectors for the homepage
TOP_TAGS_SELECTOR = ".tag-item a"  # Selects all tag links in the tag cloud

# Selectors for the quotes page
QUOTE_SELECTOR = ".quote"  # Selects all quote containers
QUOTE_TEXT_SELECTOR = ".text"  # Selects the quote text within a quote container
QUOTE_AUTHOR_SELECTOR = ".author"  # Selects the author name within a quote container
QUOTE_TAGS_SELECTOR = ".tags .tag"  # Selects all tags within a quote container

# Selector for pagination
NEXT_PAGE_SELECTOR = ".next a"  # Selects the "Next" button for pagination
