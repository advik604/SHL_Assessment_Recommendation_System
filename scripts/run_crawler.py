from src.data.crawler import SHLCrawler

crawler = SHLCrawler()
df = crawler.crawl()

df.to_csv("data/processed/catalog.csv", index=False)
print(f"Saved {len(df)} assessments. Ensure >=377 before submission.")