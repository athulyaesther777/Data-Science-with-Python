This script demonstrates basic data manipulation using Pandas, including creating DataFrames, filtering data, and performing operations on columns.

```python
import pandas as pd

# Creating a DataFrame
data = {'A': [1, 2, 3, 4], 'B': [5, 6, 7, 8]}
df = pd.DataFrame(data)
print(df)

# Filtering rows where column 'A' is greater than 2
filtered_df = df[df['A'] > 2]
print(filtered_df)

# Adding a new column
df['C'] = df['A'] + df['B']
print(df)
