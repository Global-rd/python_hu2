def get_top10_tag_xpath() -> str:
    return '//span[@class="tag-item"]/a'

def get_author_xpath() -> str:
    return '//div[@class="quote"]/span/small[@class="author"]'

def get_quote_xpath() -> str:
    return '//div[@class="quote"]/span[@class="text"]'

def get_next_link() -> str:
    return '//nav/ul/li[@class="next"]/a/@href'

