import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Load logistics dataset
df = pd.read_csv("logistics_orders_raw.csv")

# Display dataset information
print("Original Data:")
print(df.head())

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Remove duplicate records
df = df.drop_duplicates()

# Handle missing values
df = df.fillna({
    "quantity": df["quantity"].median(),
    "transportation_cost": df["transportation_cost"].median()
})

# Detect outliers using IQR
Q1 = df["transportation_cost"].quantile(0.25)
Q3 = df["transportation_cost"].quantile(0.75)
IQR = Q3 - Q1

outliers = df[
    (df["transportation_cost"] < Q1 - 1.5 * IQR) |
    (df["transportation_cost"] > Q3 + 1.5 * IQR)
]

print("\nPotential Outliers:")
print(outliers)

# Normalize numeric data
scaler = MinMaxScaler()
df["normalized_cost"] = scaler.fit_transform(
    df[["transportation_cost"]]
)

# Save cleaned dataset
df.to_csv("logistics_orders_cleaned.csv", index=False)

print("\nData preprocessing completed!")
