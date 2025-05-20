def get_top10_tag_div() -> str:
    return '//div[@class="col-md-4 tags-box"]'

def get_tag_item() -> str:
    return '//span[@class="tag-item"]/a[@class="tag"]'

def get_quote_xpath() -> str:
    return '//div[@class="quote"]/span[@class="text"]'

def get_next_link() -> str:
    return '//nav/ul/li[@class="next"]/a/@href'

