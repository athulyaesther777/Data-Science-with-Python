import pandas as pd

# Reading a CSV file
df = pd.read_csv('data.csv')
print(df.head())

# Writing to a CSV file
df.to_csv('output.csv', index=False)
