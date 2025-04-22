from sklearn.ensemble import IsolationForest
import pandas as pd

# Sample order data
data = {
    'order_id': [1, 2, 3, 4, 5, 6, 7],
    'order_amount': [100, 150, 120, 180, 220, 1000, 250],
    'order_frequency': [2, 3, 2, 3, 4, 1, 2]
}

df = pd.DataFrame(data)

# Only use DataFrame with column names for fitting & predicting
features = df[['order_amount', 'order_frequency']]

model = IsolationForest(contamination=0.1, random_state=42)
df['anomaly'] = model.fit_predict(features)

# Mark anomalies
df['is_anomalous'] = df['anomaly'].map({1: 'No', -1: 'Yes'})

# Print the results
print(df[['order_id', 'order_amount', 'order_frequency', 'is_anomalous']])
