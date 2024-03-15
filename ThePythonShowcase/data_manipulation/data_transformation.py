import pandas as pd

# Load data
df = pd.read_csv('path/to/your/data.csv')

# Group data by a column and calculate the mean for each group
grouped = df.groupby('column_name').mean()

# Sort data by a column
sorted_df = df.sort_values(by='column_name', ascending=False)

# Apply a function to each row
df['new_column'] = df['existing_column'].apply(lambda x: x * 10)
