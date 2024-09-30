import pandas as pd

df = pd.read_csv('laptop_price - dataset.csv')
print(df.head(5))
print(df.info())
print(df.describe())