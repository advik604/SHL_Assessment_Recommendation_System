import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import pandas as pd
import time

class SHLCrawler:
    def __init__(self):
        self.base = "https://www.shl.com"
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "Mozilla/5.0"
        })

        self.seed_urls = [
            "https://www.shl.com/products/assessments/behavioral-assessments/",
            "https://www.shl.com/products/assessments/assessment-and-development-centers/",
            "https://www.shl.com/products/assessments/personality-assessment/",
            "https://www.shl.com/products/assessments/cognitive-assessments/",
            "https://www.shl.com/products/assessments/skills-and-simulations/",
            "https://www.shl.com/products/assessments/job-focused-assessments/",
        ]

        self.visited = set()
        self.product_urls = set()

    def is_valid_link(self, url):
        return (
            url.startswith("https://www.shl.com/products/")
            and not url.endswith(".pdf")
            and "book-a-demo" not in url
            and "contact" not in url
        )

    def is_product_page(self, soup):
        return soup.find("div", class_="product-catalogue module") is not None

    def crawl(self):
        queue = list(self.seed_urls)

        while queue:
            url = queue.pop(0)

            if url in self.visited:
                continue

            self.visited.add(url)

            try:
                response = self.session.get(url, timeout=10)
                response.raise_for_status()
            except:
                continue

            soup = BeautifulSoup(response.text, "html.parser")

            # If this is a real product page, store it
            if self.is_product_page(soup):
                self.product_urls.add(url)
                print(f"Found product: {url}")
                continue

            # Otherwise, discover more links
            for a in soup.find_all("a", href=True):
                full_url = urljoin(self.base, a["href"])

                if self.is_valid_link(full_url) and full_url not in self.visited:
                    queue.append(full_url)

            time.sleep(0.5)

        print(f"\nTotal product URLs found: {len(self.product_urls)}")

        return self.scrape_products()

    def scrape_products(self):
        data = []

        for url in self.product_urls:
            try:
                response = self.session.get(url, timeout=10)
                soup = BeautifulSoup(response.text, "html.parser")

                name = soup.find("h1").get_text(strip=True)

                description = ""
                desc_block = soup.find("div", class_="product-catalogue-training-calendar__row typ")
                if desc_block:
                    description = desc_block.get_text(" ", strip=True)

                data.append({
                    "name": name,
                    "url": url,
                    "description": description
                })

                print(f"Scraped: {name}")

                time.sleep(0.5)

            except:
                continue

        df = pd.DataFrame(data)
        df.to_csv("data/raw/assessments.csv", index=False)

        print(f"\nSaved {len(df)} assessments.")
        return df