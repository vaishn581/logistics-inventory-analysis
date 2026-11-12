import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("logistics_data.csv")

print("Dataset information:")
df.info()
print("\nDescriptive statistics:")
print(df.describe())
print("\nMean:\n", df.mean(numeric_only=True))
print("\nMedian:\n", df.median(numeric_only=True))
print("\nStandard deviation:\n", df.std(numeric_only=True))

numeric_cols = ["delivery_days", "shipment_volume", "transportation_cost"]
corr = df[numeric_cols].corr()
print("\nCorrelation matrix:\n", corr)

destination = df.groupby("destination").agg({
    "delivery_days": "mean",
    "transportation_cost": "mean",
    "shipment_volume": "mean"
})
print("\nDestination-wise analysis:\n", destination.round(2))

plt.figure(figsize=(8, 5))
destination["delivery_days"].plot(kind="bar")
plt.title("Average Delivery Days by Destination")
plt.xlabel("Destination")
plt.ylabel("Average Delivery Days")
plt.xticks(rotation=25)
plt.tight_layout()
plt.savefig("delivery_trends.png")
plt.show()

plt.figure(figsize=(8, 5))
plt.hist(df["transportation_cost"], bins=6, edgecolor="black")
plt.title("Transportation Cost Distribution")
plt.xlabel("Transportation Cost")
plt.ylabel("Number of Orders")
plt.tight_layout()
plt.savefig("cost_distribution.png")
plt.show()

plt.figure(figsize=(8, 5))
plt.scatter(df["shipment_volume"], df["transportation_cost"])
plt.title("Shipment Volume vs Transportation Cost")
plt.xlabel("Shipment Volume")
plt.ylabel("Transportation Cost")
plt.tight_layout()
plt.savefig("shipment_analysis.png")
plt.show()

plt.figure(figsize=(8, 5))
sns.heatmap(corr, annot=True, cmap="coolwarm", linewidths=0.5)
plt.title("Logistics Data Correlation Heatmap")
plt.tight_layout()
plt.savefig("correlation_heatmap.png")
plt.show()
