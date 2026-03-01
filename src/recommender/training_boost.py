import pandas as pd


def extract_slug(url):
    return url.strip().lower().rstrip("/").split("/")[-1]


def build_slug_boost_map(excel_path="Gen_AI_Dataset.xlsx"):
    train = pd.read_excel(excel_path, sheet_name="Train-Set")

    role_slug_map = {}

    for _, row in train.iterrows():
        query = row["Query"].lower()
        slug = extract_slug(row["Assessment_url"])

        # Simple role detection
        role_keywords = [
            "consultant",
            "developer",
            "engineer",
            "manager",
            "analyst",
            "sales"
        ]

        for role in role_keywords:
            if role in query:
                if role not in role_slug_map:
                    role_slug_map[role] = {}
                role_slug_map[role][slug] = role_slug_map[role].get(slug, 0) + 1

    return role_slug_map