import json
import re
import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

session = requests.Session()
retries = Retry(total=3, backoff_factor=1, status_forcelist=[500, 502, 503, 504])
session.mount("https://", HTTPAdapter(max_retries=retries))
session.headers.update({"User-Agent": "Mozilla/5.0"})

BASE = "https://quotes.toscrape.com/js/"


def extract_quotes(html):
    soup = BeautifulSoup(html, "html.parser")
    script = soup.find("script", string=lambda s: bool(s and "var data" in s))
    if script is None or script.string is None:
        return []
    match = re.search(r"var data = (\[.*?\]);", script.string, re.DOTALL)
    if match is None:
        return []
    return json.loads(match.group(1))


all_quotes = []
page = 1
while True:
    url = BASE if page == 1 else f"{BASE}page/{page}/"
    response = session.get(url, timeout=(5, 30))

    if response.status_code == 404:
        break

    response.encoding = "utf-8"
    quotes = extract_quotes(response.text)
    if not quotes:
        break

    all_quotes.extend(quotes)
    print(f"page {page}: {len(all_quotes)} quotes so far")
    page += 1
    time.sleep(0.5)

df = pd.json_normalize(all_quotes)
df = df.rename(columns={"author.name": "author", "author.slug": "author_slug",
                        "author.goodreads_link": "author_link"})
df["tags"] = df["tags"].apply(lambda t: ", ".join(t))

print(df.shape)
print(df.head())

df.to_csv("quotes.csv", index=False, encoding="utf-8")
df.to_json("quotes.json", orient="records", indent=2, force_ascii=False)

df.info()
print(df.isna().sum())