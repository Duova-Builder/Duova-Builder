import pandas as pd

# Read CSV
df = pd.read_csv("input.csv")

# Remove rows where Location contains "fixing" or "reserved"
df = df[
    ~df["Location"].str.contains(
        "fixing|reserved",
        case=False,
        na=False
    )
]

# Calculate total stock for each SKU
df["TotalStock"] = df.groupby("SKU")["Available"].transform("sum")

# Keep SKUs with total stock >= 50
result = df[df["TotalStock"] >= 50]

# Keep one row per SKU
result = result.drop_duplicates(subset="SKU", keep="first")

# Export
result.to_csv("largerThan50.csv", index=False)

print("Done. Output saved to largerThan50.csv")