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


def scrape_item(url):
    print(url)


def scrape_page(url):
    selector = Selector(text=get(url, headers=headers).text)
    products = selector.xpath(XPATHS["products"]).getall()
    for product in products:
        scrape_item(product)


for category, link in categories.items():
    for page in range(MAX_PAGES):
        scrape_page(f"{link}&page={page+1}")
