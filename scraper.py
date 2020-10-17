from parsel import Selector
from pprint import pprint
from requests import get
from re import sub

XPATHS = {
    "products": "//a[@class='product-title-link line-clamp line-clamp-2 truncate-title']/@href"
}

MAX_PAGES = 5

host = "https://www.walmart.com/"
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
}

categories = {"electronics": "https://www.walmart.com/search/?cat_id=3944"}

for category, link in categories.items():
    for page in range(MAX_PAGES):
        selector = Selector(text=get(f"{link}&page={page+1}", headers=headers).text)
        products = selector.xpath(XPATHS["products"]).getall()
        print(len(products))
        pprint(products)
