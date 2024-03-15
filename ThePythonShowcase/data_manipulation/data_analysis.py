import pandas as pd

# Load data
df = pd.read_csv('path/to/your/data.csv')

# Descriptive statistics for each column
print(df.describe())

# Correlation matrix
print(df.corr())

# Simple visualization (requires matplotlib)
df['column_name'].hist()
