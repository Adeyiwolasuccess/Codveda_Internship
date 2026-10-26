import requests
import pandas as pd
from bs4 import BeautifulSoup
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from urllib.parse import urljoin

session = requests.Session()
retries = Retry(total=3, backoff_factor=1, status_forcelist=[500, 502, 503, 504])
session.mount("https://", HTTPAdapter(max_retries=retries))
session.headers.update({"User-Agent": "Mozilla/5.0"})

BASE = "https://books.toscrape.com/"
rating_map = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}


def parse_page(soup, page_url):
    items = []
    for book in soup.find_all("article", class_="product_pod"):
        title_tag = book.select_one("h3 a")
        price_tag = book.select_one("p.price_color")
        rating_tag = book.select_one("p.star-rating")
        avail_tag = book.select_one("p.availability")

        if not (title_tag and price_tag and rating_tag and avail_tag):
            continue

        items.append({
            "title": title_tag["title"],
            "price": float(price_tag.text.replace("£", "")),
            "rating": rating_map[rating_tag["class"][1]],
            "availability": avail_tag.text.strip(),
            "link": urljoin(page_url, str(title_tag["href"])),
        })
    return items


data = []
page = 1
while True:
    url = BASE if page == 1 else f"{BASE}catalogue/page-{page}.html"
    response = session.get(url, timeout=(5, 30))

    if response.status_code == 404:
        break

    response.encoding = "utf-8"
    soup = BeautifulSoup(response.text, "html.parser")
    data.extend(parse_page(soup, url))

    print(f"page {page}: {len(data)} books so far")
    page += 1

df = pd.DataFrame(data)
print(df.shape)
print(df.head())

df.to_csv("books.csv", index=False, encoding="utf-8")
df.to_json("books.json", orient="records", indent=2, force_ascii=False)

df.info()
print(df.isna().sum())