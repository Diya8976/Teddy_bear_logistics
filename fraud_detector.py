import pandas as pd
from sklearn.ensemble import IsolationForest

def detect_fake_deliveries():
    df = pd.read_csv("delivery_tracking.csv")
    
    if 'start_time' not in df.columns:
        raise KeyError("Missing 'start_time' column in the CSV file.")
    if 'teddy_id' not in df.columns:
        raise KeyError("Missing 'teddy_id' column in the CSV file.")
    
    df["delivery_time"] = (pd.to_datetime(df["actual_delivery"]) - pd.to_datetime(df["start_time"])).dt.total_seconds() / 3600

    clf = IsolationForest(contamination=0.1, random_state=42)
    df["anomaly_score"] = clf.fit_predict(df[["delivery_time"]])
    df["suspected"] = df["anomaly_score"] == -1
    
    frauds = df[df["suspected"]]
    frauds[["teddy_id", "delivery_time", "suspected"]].to_csv("fraud_logs.csv", index=False)
    print(f"[✔] Detected {len(frauds)} suspicious deliveries!")

if __name__ == "__main__":
    detect_fake_deliveries()