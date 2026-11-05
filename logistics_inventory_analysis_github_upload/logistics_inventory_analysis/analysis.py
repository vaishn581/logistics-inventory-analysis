"""
Logistics and Inventory Management Analysis
Beginner-friendly sample project using Python, Pandas and Matplotlib.

Note: The included dataset is fictional sample data created for learning.
Replace it with a real, properly licensed dataset before making real-world claims.
"""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

DATA_PATH = Path(__file__).parent / "data" / "logistics_orders.csv"
OUTPUT_DIR = Path(__file__).parent / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

# 1. Load data
df = pd.read_csv(DATA_PATH, parse_dates=["order_date"])

# 2. Basic cleaning
df = df.drop_duplicates(subset="order_id")
df["transport_cost_inr"] = pd.to_numeric(df["transport_cost_inr"], errors="coerce")
df["delivery_days"] = pd.to_numeric(df["delivery_days"], errors="coerce")
df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce")
df["on_time"] = pd.to_numeric(df["on_time"], errors="coerce")
df = df.dropna(subset=["transport_cost_inr", "delivery_days", "quantity", "on_time"])

# 3. Calculate KPIs
total_orders = len(df)
on_time_rate = df["on_time"].mean() * 100
average_delivery_days = df["delivery_days"].mean()
average_transport_cost = df["transport_cost_inr"].mean()
total_quantity = df["quantity"].sum()

print("LOGISTICS KPI SUMMARY")
print("---------------------")
print(f"Total orders: {total_orders}")
print(f"On-time delivery rate: {on_time_rate:.1f}%")
print(f"Average delivery time: {average_delivery_days:.2f} days")
print(f"Average transport cost: INR {average_transport_cost:.2f}")
print(f"Total quantity shipped: {total_quantity}")

# 4. Explore cost by destination
cost_by_destination = (
    df.groupby("destination")["transport_cost_inr"]
      .mean()
      .sort_values(ascending=False)
)
print("\nAverage transport cost by destination:")
print(cost_by_destination)

# 5. Save a chart
plt.figure(figsize=(8, 5))
cost_by_destination.plot(kind="bar")
plt.title("Average Transportation Cost by Destination")
plt.xlabel("Destination")
plt.ylabel("Average cost (INR)")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "average_cost_by_destination.png")
plt.close()

# 6. Save cleaned data and KPI summary
df.to_csv(OUTPUT_DIR / "cleaned_logistics_orders.csv", index=False)
kpis = pd.DataFrame({
    "KPI": [
        "Total Orders", "On-time Delivery Rate (%)",
        "Average Delivery Time (days)", "Average Transport Cost (INR)",
        "Total Quantity Shipped"
    ],
    "Value": [
        total_orders, round(on_time_rate, 2), round(average_delivery_days, 2),
        round(average_transport_cost, 2), total_quantity
    ]
})
kpis.to_csv(OUTPUT_DIR / "kpi_summary.csv", index=False)

print(f"\nFiles saved in: {OUTPUT_DIR}")
