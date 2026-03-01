class Settings:
    BASE_URL = "https://www.shl.com/solutions/products/product-catalog/"
    DATA_PATH = "data/processed/catalog.csv"
    EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
    TOP_K = 10

settings = Settings()