import pandas as pd

print("Loading dataset from CSV file...\n")
df = pd.read_csv("data.csv")

print("First 5 rows:")
print(df.head())
print()

print("Last 5 rows:")
print(df.tail())
print()

print("Dataset Info:")
df.info()
print()

print("Summary Statistics:")
print(df.describe())
print()

age_column = df["Age"]
print("Single Column Selected (Age):")
print(age_column)
print()

selected_columns = df[["Name", "Score"]]
print("Multiple Columns Selected (Name and Score):")
print(selected_columns)
print()

filtered_rows = df[df["Score"] > 80]
print("Filtered Rows (Score > 80):")
print(filtered_rows)