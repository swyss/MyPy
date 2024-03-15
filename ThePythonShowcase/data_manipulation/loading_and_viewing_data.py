import pandas as pd
import matplotlib.pyplot as plt

# Load a CSV file into a DataFrame
df = pd.read_csv('./assets/data_TESLA.csv')

# View the first few rows of the DataFrame
print(df.head())

# Basic information about the DataFrame
print(df.info())

# Summary statistics for numerical columns
print(df.describe())

# Grouping and aggregation
grouped_df = df.groupby('Date').mean()
print(grouped_df)

# Data cleaning: removing missing values
clean_df = df.dropna()

# Data transformation: creating a new column
df['new_column'] = df['High'] * 10
print(df.head())

# Histogram of a numerical column
df['new_column'].hist()


# # Bar plot of a categorical column
# df['categorical_column'].value_counts().plot(kind='bar')

# plt.show()
# # Data analysis: correlation matrix
# print(df.corr())
#
# # Data analysis: value counts for a categorical column
# print(df['categorical_column'].value_counts())


def load_and_view_data(file_path):
    df = pd.read_csv(file_path)
    print("First five rows of the dataset:")
    print(df.head())
    return df


def load_clean_and_view_data(file_path):
    df = pd.read_csv(file_path)
    print("First five rows of the dataset:")
    print(df.head())
    # Data cleaning
    df_clean = df.dropna()
    print("\nData after cleaning:")
    print(df_clean.info())
    # Data transformation
    grouped_df = df_clean.groupby('High').mean()
    print("\nData after transformation (grouping and mean):")
    print(grouped_df.head())
    return df_clean, grouped_df


def load_clean_transform_analyze_and_visualize_data(file_path):
    # Load data
    df = pd.read_csv(file_path)
    print("First five rows of the dataset:")
    print(df.head())

    # Data cleaning
    df_clean = df.dropna()
    print("\nData after cleaning:")
    print(df_clean.info())

    # Data transformation
    grouped_df = df_clean.groupby('category').mean()
    print("\nData after transformation (grouping and mean):")
    print(grouped_df.head())

    # Data analysis
    print("\nDescriptive statistics of the dataset:")
    print(df_clean.describe())

    # Data visualization
    df_clean['numeric_column'].hist()
    plt.show()

    return df_clean, grouped_df


if __name__ == "__main__":
    file_path = './assets/data_TESLA.csv'
    load_and_view_data(file_path)

    load_clean_and_view_data(file_path)

    load_clean_transform_analyze_and_visualize_data(file_path)
