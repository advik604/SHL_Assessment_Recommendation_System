import pandas as pd

df = pd.read_csv("submission.csv")

print("Columns:", df.columns.tolist())
print("Total rows:", len(df))
print("Unique queries:", df["Query"].nunique())
print("Rows per query:", len(df) / df["Query"].nunique())