from flask import Flask, render_template, jsonify
import pandas as pd
import json
from sklearn.ensemble import IsolationForest
import plotly.express as px
import plotly.io as pio

# Flask app initialization
app = Flask(__name__)

# Load preprocessed data (use the appropriate file paths)
df_orders = pd.read_csv('delivery_updates.csv')

# Initialize the Isolation Forest model (fraud detection)
model = IsolationForest(contamination=0.1)
model.fit(df_orders[['order_amount', 'delivery_status_code']])

# Apply anomaly detection
df_orders['anomaly'] = model.predict(df_orders[['order_amount', 'delivery_status_code']])
df_orders['is_anomalous'] = df_orders['anomaly'].apply(lambda x: 'Yes' if x == -1 else 'No')

# Plot top order performance (bar chart)
fig_orders = px.bar(df_orders, x='order_id', y='order_amount', color='is_anomalous',
                    title="Order Amounts with Anomalies (Fake Deliveries)")
pio.write_html(fig_orders, file='templates/orders_viz.html')

# Define routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/orders')
def orders():
    return render_template('orders_viz.html')

@app.route('/fraud_detection')
def fraud_detection():
    # Get fraudulent orders as JSON
    fraud_orders = df_orders[df_orders['is_anomalous'] == 'Yes'].to_dict(orient='records')
    return jsonify(fraud_orders)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
