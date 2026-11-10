import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split, cross_val_score, KFold
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Generate hypothetical logistics dataset
np.random.seed(42)

n = 1200

distance = np.random.uniform(5, 500, n)
weight = np.random.uniform(0.5, 1200, n)

traffic = np.random.choice(
    ["Low", "Medium", "High"], n
)

weather = np.random.choice(
    ["Clear", "Rain", "Storm"], n
)

vehicle = np.random.choice(
    ["Bike", "Van", "Truck"], n
)

priority = np.random.choice(
    ["Standard", "Express"], n
)

traffic_effect = pd.Series(traffic).map({
    "Low": 0, "Medium": 18, "High": 42
}).values

weather_effect = pd.Series(weather).map({
    "Clear": 0, "Rain": 14, "Storm": 35
}).values

vehicle_effect = pd.Series(vehicle).map({
    "Bike": 6, "Van": 0, "Truck": 9
}).values

priority_effect = pd.Series(priority).map({
    "Standard": 8, "Express": -4
}).values

delivery_time = (
    1.2 + distance / 48 + weight / 900
    + traffic_effect / 60
    + weather_effect / 60
    + vehicle_effect / 60
    + priority_effect / 60
    + np.random.normal(0, 18, n) / 60
)

data = pd.DataFrame({
    "distance_km": distance,
    "shipment_weight_kg": weight,
    "traffic_level": traffic,
    "weather": weather,
    "vehicle_type": vehicle,
    "priority": priority,
    "delivery_time_hours": delivery_time
})

# Separate features and target
X = data.drop(columns=["delivery_time_hours"])
y = data["delivery_time_hours"]

# Preprocessing
numeric = ["distance_km", "shipment_weight_kg"]

categorical = [
    "traffic_level", "weather",
    "vehicle_type", "priority"
]

preprocess = ColumnTransformer([
    ("num", SimpleImputer(strategy="median"), numeric),
    ("cat", Pipeline([
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("encoder", OneHotEncoder(handle_unknown="ignore"))
    ]), categorical)
])

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42
)

# Train models
models = {
    "Linear Regression": LinearRegression(),
    "Random Forest": RandomForestRegressor(
        n_estimators=250,
        max_depth=12,
        min_samples_leaf=3,
        random_state=42
    )
}

for name, model in models.items():

    pipeline = Pipeline([
        ("preprocessing", preprocess),
        ("model", model)
    ])

    pipeline.fit(X_train, y_train)

    predictions = pipeline.predict(X_test)

    print("\nModel:", name)

    print("MAE:", mean_absolute_error(
        y_test, predictions
    ))

    print("RMSE:", np.sqrt(
        mean_squared_error(y_test, predictions)
    ))

    print("R2 Score:", r2_score(
        y_test, predictions
    ))

# Cross Validation
rf_pipeline = Pipeline([
    ("preprocessing", preprocess),
    ("model", models["Random Forest"])
])

scores = cross_val_score(
    rf_pipeline,
    X_train,
    y_train,
    cv=KFold(n_splits=5, shuffle=True, random_state=42),
    scoring="neg_mean_absolute_error"
)

print("\nCross Validation MAE:", -scores.mean())

print("\nLogistics Prediction Completed Successfully!")

