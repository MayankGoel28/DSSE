from parsel import Selector
from pprint import pprint
from requests import get
from re import sub

XPATHS = {
    "products": "//a[@class='product-title-link line-clamp line-clamp-2 truncate-title']/@href",
    "title": "//h1[@class='prod-ProductTitle prod-productTitle-buyBox font-bold']/text()",
    "price": "//span[@class='price display-inline-block arrange-fit price price--stylized']/span[@class='visuallyhidden']/text()",
    "stars": "//span[@itemprop='ratingValue']/text()",
    "ratings": "//span[@class='stars-reviews-count-node']/text()",
    "img": "//img[@class='hover-zoom-hero-image']/@src",
    "tags": "//ul[@class='IpsumModuleLinksWrapper-desktop-link']/li/a/text()",
}

MAX_PAGES = 5

host = "https://www.walmart.com"

categories = {"electronics": "https://www.walmart.com/search/?cat_id=3944"}


def scrape_item(url):
    title = None
    while not title:
        text = get(url).text
        selector = Selector(text=text)
        img = selector.xpath(XPATHS["img"]).get()
        tags = selector.xpath(XPATHS["tags"]).getall()
        title = selector.xpath(XPATHS["title"]).get()
        price = selector.xpath(XPATHS["price"]).get()
        stars = selector.xpath(XPATHS["stars"]).get()
        ratings = selector.xpath(XPATHS["ratings"]).get()

    item = {
        "title": title,
        "price": price,
        "stars": stars if stars else 0,
        "ratings": ratings[:-7] if stars else 0,
        "img": img[2:] if img else "",
        "tags": tags,
    }

    pprint(item)


def scrape_page(url):
    text = get(url).text
    selector = Selector(text=text)
    products = selector.xpath(XPATHS["products"]).getall()
    for product in products:
        scrape_item(f"{host}{product}")


for category, link in categories.items():
    for page in range(MAX_PAGES):
        scrape_page(f"{link}&page={page+1}")
