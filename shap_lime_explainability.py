import shap
import pandas as pd
from sklearn.ensemble import IsolationForest

# Sample data (replace with actual data)
data = {
    'order_amount': [100, 150, 120, 180, 220, 1000],
    'delivery_status': [1, 1, 1, 0, 1, 1]
}

df = pd.DataFrame(data)

# Fit an Isolation Forest model
model = IsolationForest(contamination=0.1)
model.fit(df)

# Use SHAP for model interpretability
explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(df)

# Plot SHAP values
shap.summary_plot(shap_values, df)
