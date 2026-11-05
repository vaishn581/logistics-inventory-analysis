# Logistics and Inventory Management Analysis Using Python

## Project overview
This beginner-level project explores a small logistics orders dataset and calculates useful performance indicators (KPIs). It demonstrates data loading, cleaning, grouping, KPI calculation, and a basic chart using Python.

**Important:** `data/logistics_orders.csv` contains fictional sample data for practice. It is not real company or industry data.

## Objectives
- Measure on-time delivery performance.
- Calculate average delivery time and transportation cost.
- Compare average transportation cost across destinations.
- Save cleaned data, KPI results, and a chart.

## KPIs
1. **On-Time Delivery Rate:** percentage of orders marked as delivered on time.
2. **Average Delivery Time:** average number of days taken for delivery.
3. **Average Transportation Cost:** average transport cost per order in INR.
4. **Total Quantity Shipped:** sum of quantities across orders.

## Tools and libraries
- Python 3
- Pandas
- Matplotlib

## Project structure
```text
logistics_inventory_analysis/
├── data/
│   └── logistics_orders.csv
├── outputs/                 # created when the script runs
├── analysis.py
├── requirements.txt
└── README.md
```

## How to run
1. Install Python 3.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Run:
   ```bash
   python analysis.py
   ```

The script prints the KPI summary and creates an `outputs` folder containing:
- `kpi_summary.csv`
- `cleaned_logistics_orders.csv`
- `average_cost_by_destination.png`

## Methodology
1. Load the CSV dataset with Pandas.
2. Remove duplicate order IDs.
3. Convert numeric columns and remove rows with missing KPI values.
4. Calculate the KPIs.
5. Group records by destination to compare transportation costs.
6. Visualize the comparison with a bar chart.

## Future improvements
- Use a larger real-world dataset from a reliable public source.
- Add inventory stock and reorder-level data.
- Explore demand forecasting with regression.
- Compare delivery patterns using clustering.
- Study route optimization using appropriate optimization methods.

## Data source
The sample data was manually created for this educational demonstration. It is fictional and should not be treated as actual logistics performance data.
