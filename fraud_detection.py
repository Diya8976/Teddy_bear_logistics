from sklearn.ensemble import IsolationForest
import pandas as pd

# Simulate delivery data (e.g., delivery times, distances, etc.)
data = {
    'delivery_time': [1, 2, 3, 50, 5, 100, 6, 7, 8],
    'distance': [10, 20, 30, 40, 50, 60, 70, 80, 90],
}

df = pd.DataFrame(data)

# Fit Isolation Forest model
model = IsolationForest(contamination=0.2)  # 20% of data considered anomalous
model.fit(df)

# Predict anomalies
df['anomaly'] = model.predict(df)

# Anomalies are labeled as -1
print("Anomalous Deliveries Detected:")
print(df[df['anomaly'] == -1])
