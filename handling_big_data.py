import pandas as pd

# Reading a large CSV file in chunks
chunk_size = 1000
for chunk in pd.read_csv('largefile.csv', chunksize=chunk_size):
    print(chunk.head())
