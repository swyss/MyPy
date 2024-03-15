import pandas as pd

# Load data
df = pd.read_csv('path/to/your/data.csv')

# Drop rows with missing values
df_clean = df.dropna()

# Fill missing values with the mean of the column
df_filled = df.fillna(df.mean())

# Filter rows based on a condition
df_filtered = df[df['column_name'] > some_value]
