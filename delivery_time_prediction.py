import xgboost as xgb
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

# Load historical delivery data (simulated for this example)
# In a real-world scenario, you'll gather actual delivery data
data = {
    'distance_km': [10, 20, 30, 40, 50],
    'traffic_condition': [1, 2, 3, 2, 1],  # 1: Low, 2: Medium, 3: High
    'delivery_time_hours': [1, 2, 3, 4, 5]
}

df = pd.DataFrame(data)

# Split data into features (X) and target (y)
X = df.drop('delivery_time_hours', axis=1)
y = df['delivery_time_hours']

# Split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train XGBoost model
model = xgb.XGBRegressor(objective='reg:squarederror', n_estimators=100, learning_rate=0.1)
model.fit(X_train, y_train)

# Predict on test data
y_pred = model.predict(X_test)

# Evaluate the model
mae = mean_absolute_error(y_test, y_pred)
print(f"Mean Absolute Error: {mae}")

# Predict delivery time for a new set of conditions
new_data = np.array([[25, 2]])  # 25 km, medium traffic
predicted_time = model.predict(new_data)
print(f"Predicted Delivery Time: {predicted_time[0]} hours")
