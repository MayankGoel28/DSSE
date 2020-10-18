from parsel import Selector
from pprint import pprint
from requests import get
from json import dump
from re import sub

MAX_PAGES = 1

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

categories = {
    "electronics": "https://www.walmart.com/search/?cat_id=3944&sort=best_seller",
    "food": "https://www.walmart.com/search/?cat_id=976759&sort=best_seller",
    "personal_care": "https://www.walmart.com/search/?cat_id=976759&&sort=best_seller",
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


def scrape_page(url):
    text = get(url).text
    selector = Selector(text=text)
    products = selector.xpath(XPATHS["products"]).getall()
    page = [scrape_item(f"{host}{product}") for product in products]

    return page


if __name__ == "__main__":
    for category, link in categories.items():
        print(f"Now scraping: {category}")
        for pagenum in range(MAX_PAGES):
            print(f"Page: {pagenum+1}")

            try:
                for trail in range(3):
                    page = scrape_page(f"{link}&page={pagenum+1}")

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
