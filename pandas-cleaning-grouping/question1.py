import pandas as pd
import numpy as np

data = {
    "Employee": [
        "Amit", "Neha", "Rahul", "Sneha",
        "Vikram", "Priya", "Arjun", "Divya"
    ],
    "Department": [
        "IT", "HR", "IT", "Finance",
        "HR", "Finance", "IT", "HR"
    ],
    "Salary": [
        600000, 500000, np.nan, 700000,
        520000, np.nan, 650000, 480000
    ],
    "Temporary_Notes": [
        "On probation", "Contract",
        "Pending docs", "Verified",
        "Intern", "New joiner",
        "On leave", "Temporary role"
    ]
}

df = pd.DataFrame(data)

print("Missing Values in Dataset:\n")
print(df.isnull())
print()

print("Number of Missing Values:\n")
print(df.isnull().sum())
print()

mean_salary = df["Salary"].mean()
df["Salary"].fillna(mean_salary, inplace=True)

print("DataFrame :\n")
print(df)
print()

df = df.drop(columns=["Temporary_Notes"])

print("DataFrame :\n")
print(df)
print()

df = df.rename(columns={"Salary": "Annual_Salary"})

print("DataFrame :\n")
print(df)
print()

summary = df.groupby("Department").agg(
    Mean_Salary=("Annual_Salary", "mean"),
    Employee_Count=("Employee", "count")
)

print("final summary table :\n")
print(summary)