from parsel import Selector
from pprint import pprint
from requests import get
from json import dump
from re import sub
from functools import wraps
import errno
import os
import signal

MAX_PAGES = 25

XPATHS = {
    "products": "//a[@class='product-title-link line-clamp line-clamp-2 truncate-title']/@href",
    "title": "//h1[@class='prod-ProductTitle prod-productTitle-buyBox font-bold']/text()",
    "price": "//span[@class='price display-inline-block arrange-fit price price--stylized']/span[@class='visuallyhidden']/text()",
    "stars": "//span[@itemprop='ratingValue']/text()",
    "ratings": "//span[@class='stars-reviews-count-node']/text()",
    "img": "//img[@class='hover-zoom-hero-image']/@src",
    "tags": "//ul[@class='IpsumModuleLinksWrapper-desktop-link']/li/a/@href",
    "related": "//ul[@class='IpsumModuleLinksWrapper-desktop-link']/li/a/text()",
    "about": "//*[@id='about-product-section']/div/div[1]/div[1]/div[3]/text()"
}

host = "https://www.walmart.com"

linkfile = "links/personalcare.txt"

class TimeoutError(Exception):
    pass

def timeout(seconds=10, error_message=os.strerror(errno.ETIME)):
    def decorator(func):
        def _handle_timeout(signum, frame):
            raise TimeoutError(error_message)

        def wrapper(*args, **kwargs):
            signal.signal(signal.SIGALRM, _handle_timeout)
            signal.alarm(seconds)
            try:
                result = func(*args, **kwargs)
            finally:
                signal.alarm(0)
            return result

        return wraps(func)(wrapper)

    return decorator


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
        related = selector.xpath(XPATHS["related"]).getall()
        about = selector.xpath(XPATHS["about"]).get()

    item = {
        "title": title,
        "url": url,
        "price": price,
        "stars": stars if stars else 0,
        "ratings": ratings[:-7] if stars else 0,
        "img": img[2:] if img else "",
        "tags": [(tagname, tag) for tagname, tag in zip(related, tags)],
    }

    return item

@timeout(60)
def scrape_page(url):
    text = get(url).text
    selector = Selector(text=text)
    products = selector.xpath(XPATHS["products"]).getall()
    page = [scrape_item(f"{host}{product}") for product in products]

    return page


if __name__ == "__main__":
    with open(linkfile, "r") as scrapfile:
        for index, link in enumerate(scrapfile):
            # Remove \n
            link = link[:-1]
            print(f"Now scraping: {link}")
            for pagenum in range(MAX_PAGES):
                print(f"Page: {pagenum+1}")

                category = linkfile.split("/")[-1].split(".")[0] + f"{index + 1}"
                try:
                    for trail in range(5):
                        page = scrape_page(f"{link}?page={pagenum+1}")

                        if page:
                            with open(f"{category}-{pagenum+1}.json", "w") as page_json:
                                dump(page, page_json, indent=4, separators=(",", ": "))
                            print("Done!\n")
                            break
                        else:
                            print(f"Failure: {trail}")

                    if not page:
                        with open("failure.log", "a") as failure_log:
                            failure_log.write(f"{link}&page={pagenum+1}\n")
                        print("Failed! Written to logs.\n")

                except Exception as e:
                    print("Something went wrong.")
                    print(e)

        print("gg.")
