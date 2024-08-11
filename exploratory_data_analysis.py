import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('data.csv')

# Summary statistics
print(df.describe())

# Histogram of a column
df['column_name'].hist()
plt.title('Histogram of column_name')
plt.show()

# Scatter plot of two columns
plt.scatter(df['column1'], df['column2'])
plt.xlabel('Column 1')
plt.ylabel('Column 2')
plt.title('Scatter plot of Column 1 vs Column 2')
plt.show()
