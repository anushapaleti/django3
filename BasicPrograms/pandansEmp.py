import pandas as pd

# Creating a DataFrame from a dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 22, 35],
    'Grade': [85, 92, 78, 88]
}

df = pd.DataFrame(data)

# Displaying the DataFrame
print("DataFrame:")
print(df)
print()

# Basic statistics on numerical columns
print("Basic Statistics:")
print(df.describe())
print()

# Filtering data based on conditions
print("Filtered Data:")
filtered_df = df[df['Age'] > 25]
print(filtered_df)
print()

# Adding a new column
df['Status'] = ['Pass' if grade >= 80 else 'Fail' for grade in df['Grade']]

# Displaying the updated DataFrame
print("Updated DataFrame:")
print(df)
