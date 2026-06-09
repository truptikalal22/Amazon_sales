import pandas as pd

df = pd.read_csv("amazon_sales.csv")
  
print("Original shape:", df.shape)
print("\nMissing values:\n", df.isnull().sum())
print("\nDuplicate rows:", df.duplicated().sum())

df.drop_duplicates()
print("\nafter remove duplicate:\n ",df.shape)
