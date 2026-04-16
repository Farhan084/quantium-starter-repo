import pandas as pd

files = [
    "data/daily_sales_data_0.csv",
    "data/daily_sales_data_1.csv",
    "data/daily_sales_data_2.csv",
]

dfs = []
for f in files:
    df = pd.read_csv(f)
    df = df[df["product"] == "pink morsel"]
    df["price"] = df["price"].str.replace("$", "", regex=False).astype(float)
    df["sales"] = df["quantity"] * df["price"]
    dfs.append(df[["sales", "date", "region"]])

result = pd.concat(dfs, ignore_index=True)
result.to_csv("output.csv", index=False)
