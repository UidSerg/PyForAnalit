import pandas as pd
df = pd.read_csv("laptop_price.csv", sep= ',',encoding='windows-1251')
df.head(5)
df.info()
