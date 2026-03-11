import pandas as pd
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank"],
    "Score": [95, 88, 76, 92, 84, 90],
    "Passed": [True, True, False, True, True, True],
    "Category": ["A", "B", "B", "A", "C", "A"]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)
print()

print("Single Column (Score):")
score_column = df["Score"]
print(score_column)
print()

print("Multiple Columns (Name and Score):")
selected_df = df[["Name", "Score"]]
print(selected_df)
print()

print("First 3 rows using iloc:")
print(df.iloc[0:3])
print()

df_indexed = df.set_index("Name")

print("Using loc to access rows by Name:")
print(df_indexed.loc[["Alice", "David"]])
print()

print("Students with Score > 85:")
high_score = df[df["Score"] > 85]
print(high_score)
print()

print("Students with Score > 85 AND Passed = True:")
high_pass = df[(df["Score"] > 85) & (df["Passed"] == True)]
print(high_pass)
print()

print("Sorted High Performing Students:")
sorted_students = high_pass.sort_values(by="Score", ascending=False)
print(sorted_students)
print()

print("High-performing students:")
result = df[(df["Score"] > 85) & (df["Passed"])].sort_values(by="Score", ascending=False)
print(result[["Name", "Score"]])