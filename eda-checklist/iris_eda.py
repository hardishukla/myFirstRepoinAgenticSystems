import pandas as pd
import plotly.express as px

# Load dataset
df = pd.read_csv("iris.csv")

print("🔹 First 5 Rows:")
print(df.head())

print("\n🔹 Shape of Dataset:")
print(df.shape)

print("\n🔹 Column Info:")
print(df.info())

print("\n🔹 Statistical Summary:")
print(df.describe())

print("\n🔹 Missing Values:")
print(df.isnull().sum())

# -------------------------------
# Distribution of Petal Length
# -------------------------------
fig1 = px.histogram(df, x="petal_length", color="species",
                    title="Distribution of Petal Length")
fig1.show()

# -------------------------------
# Outlier Detection (Box Plot)
# -------------------------------
fig2 = px.box(df, y="petal_length", color="species",
    title="Outliers in Petal Length")
fig2.show()

# -------------------------------
# Relationship Between Variables
# -------------------------------
fig3 = px.scatter(df, x="petal_length", y="petal_width",
    color="species",
    title="Petal Length vs Petal Width")
fig3.show()

# -------------------------------
# Correlation Heatmap
# -------------------------------
corr = df.corr(numeric_only=True)
fig4 = px.imshow(corr, text_auto=True,
    title="Feature Correlation Heatmap")
fig4.show()