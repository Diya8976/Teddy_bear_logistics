from sklearn.ensemble import IsolationForest
import pandas as pd

# Sample delivery data with delivery status and order amount (replace with actual data)
data = {
    'delivery_id': [1, 2, 3, 4, 5, 6, 7],
    'order_amount': [100, 150, 120, 180, 220, 500, 1000],  # Outlier: 1000 might be suspicious
    'delivery_status': ['Delivered', 'Delivered', 'Delivered', 'Pending', 'Delivered', 'Delivered', 'Pending']  # Pending is suspicious
}

df = pd.DataFrame(data)

# Feature selection: we use 'order_amount' and 'delivery_status' for detection
df['delivery_status_code'] = df['delivery_status'].apply(lambda x: 1 if x == 'Delivered' else 0)

# Fit the Isolation Forest model
model = IsolationForest(contamination=0.1)  # Assuming 10% of deliveries are fake
df['anomaly'] = model.fit_predict(df[['order_amount', 'delivery_status_code']])

# Mark anomalies
df['is_anomalous'] = df['anomaly'].apply(lambda x: 'Yes' if x == -1 else 'No')

# Print the results
print(df[['delivery_id', 'order_amount', 'delivery_status', 'is_anomalous']])
