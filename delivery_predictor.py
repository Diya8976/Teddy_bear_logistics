import pandas as pd
from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
import joblib

def train_delivery_model():
    df = pd.read_csv("delivery_tracking.csv")
    df["delay_mins"] = (pd.to_datetime(df["actual_delivery"]) - pd.to_datetime(df["expected_delivery"])).dt.total_seconds() / 60
    
    X = df[["vehicle_id"]]  # Add more features later (route length, traffic, etc.)
    X = pd.get_dummies(X)
    y = df["delay_mins"]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    model = XGBRegressor()
    model.fit(X_train, y_train)
    
    joblib.dump(model, "delivery_time_model.pkl")
    print("[✔] Delivery prediction model trained & saved.")
    print("MAE:", mean_absolute_error(y_test, model.predict(X_test)))

if __name__ == "__main__":
    train_delivery_model()
