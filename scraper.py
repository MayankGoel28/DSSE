from parsel import Selector
from pprint import pprint
from requests import get
from json import dump
from re import sub

MAX_PAGES = 5

XPATHS = {
    "products": "//a[@class='product-title-link line-clamp line-clamp-2 truncate-title']/@href",
    "title": "//h1[@class='prod-ProductTitle prod-productTitle-buyBox font-bold']/text()",
    "price": "//span[@class='price display-inline-block arrange-fit price price--stylized']/span[@class='visuallyhidden']/text()",
    "stars": "//span[@itemprop='ratingValue']/text()",
    "ratings": "//span[@class='stars-reviews-count-node']/text()",
    "img": "//img[@class='hover-zoom-hero-image']/@src",
    "tags": "//ul[@class='IpsumModuleLinksWrapper-desktop-link']/li/a/text()",
}

host = "https://www.walmart.com"

categories = {
    "electronics": "https://www.walmart.com/search/?cat_id=3944",
    "food": "https://www.walmart.com/search/?cat_id=976759",
    "personal_care": "https://www.walmart.com/search/?cat_id=976759",
}


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

    return item


def scrape_page(url):
    text = get(url).text
    selector = Selector(text=text)
    products = selector.xpath(XPATHS["products"]).getall()
    page = []
    for product in products:
        item = scrape_item(f"{host}{product}")
        page.append(item)

    return page


for category, link in categories.items():
    print(f"Now scraping: {category}")
    for pagenum in range(MAX_PAGES):
        print(f"Page: {pagenum+1}")
        page = scrape_page(f"{link}&page={pagenum+1}")

        if page:
            with open(f"{category}-{pagenum+1}.json", "w") as page_json:
                dump(page, page_json)
            print("Done!\n")
        else:
            with open("failure.log", "a") as failure_log:
                failure_log.write(f"{link}&page={pagenum+1}\n")
            print("Failed! Written to logs.\n")

print("gg.")
