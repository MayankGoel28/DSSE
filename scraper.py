from parsel import Selector
from requests import get
from re import sub

XPATHS = {"products": "//*[@id='searchProductResult']/ul"}

MAX_PAGES = 2

host = "https://www.walmart.com/"
categories = {"electronics": "https://www.walmart.com/search/?cat_id=3944"}

for category, link in categories:
    for page in range(MAX_PAGES):
        selector = Selector(text=get(f"{link}&page={page}").text)
        products = selector.xpath(XPATHS["products"])
        for product in products:
            print(product.text)
