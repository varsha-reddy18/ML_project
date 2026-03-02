import pandas as pd

df = pd.read_csv("dataset.csv")

df = df.dropna()
df = df.drop_duplicates()

df.to_csv("clean_dataset.csv", index=False)

print("Clean dataset created!")