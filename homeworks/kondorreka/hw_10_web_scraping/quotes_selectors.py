#Top tagek megkeresése
def get_top_tags_xpath() -> str:
    return '/html/body/div/div/div/span/a'

#összes blokk megkereséde
def get_quotes_block_xpath() -> str:
    #return '//div[@class="quote"]'
    #return '/html/body/div/div[2]/div[1]/div[2]'
    return '/html/body/div/div[2]/div[1]/div'



# Blokból idézet szövege
def get_quote_text_xpath() -> str:
    return '/html/body/div/div[2]/div[1]/div/span[1]'

#blokkból a szerző neve
def get_quote_author_xpath() -> str:
    return '/html/body/div/div[2]/div[1]/div[2]/span[2]/small'

#blokkból a tag
def get_quote_tag_xpath() -> str:
    return '/html/body/div/div[2]/div[1]/div[2]/div/a'