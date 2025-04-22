import pandas as pd
from prophet import Prophet
import matplotlib.pyplot as plt

# Sample data
data = {
    'date': ['2025-01-01', '2025-01-02', '2025-01-03', '2025-01-04', '2025-01-05', '2025-01-06'],
    'orders': [10, 12, 8, 15, 20, 25]
}

df = pd.DataFrame(data)

# Prepare the data for Prophet
df = df.rename(columns={'date': 'ds', 'orders': 'y'})

# Initialize and fit the model
model = Prophet()
model.fit(df)

# Forecast for the next 30 days
future = model.make_future_dataframe(periods=30)
forecast = model.predict(future)

# Plot the forecast
fig = model.plot(forecast)
plt.title('Order Demand Prediction')
plt.show()
