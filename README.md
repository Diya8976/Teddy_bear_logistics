# Teddy_bear_logistics
# 🧸 AI-Powered Teddy Bear Logistics Tracking System

An industrial-level AI/ML project that simulates smart logistics management for teddy bear deliveries. This system combines real-time tracking, delivery performance monitoring, anomaly detection, fraud prevention, and dashboard visualization — built from scratch using Python, Streamlit, ML models, and geospatial tools.

---

## 🚀 Features

- 📋 **Attendance Tracking** – Tracks teddy bear entry/exit in warehouse using simulated RFID data.
- 🚚 **Delivery Prediction** – Predicts expected vs actual delivery time using XGBoost and regression models.
- 📊 **Demand Forecasting** – Forecasts teddy bear demand using LSTM/Prophet time series models.
- 🗺️ **Location & Geofencing** – Tracks teddy bears via GPS coordinates and geofencing alerts using Geopy.
- 🎥 **CCTV-Based Tracking** – Detects teddy bears using object detection models (YOLO/OpenCV).
- 🔍 **Fraud Detection** – Detects fake deliveries, duplicate orders, and suspicious patterns using Isolation Forest and Neo4j.
- 💬 **Email Alerts** – Sends intelligent HTML email alerts when fraud or failure is detected.
- 📈 **Interactive Dashboard** – Built using Streamlit to visualize attendance, deliveries, and anomalies.

---

## 🧠 Tech Stack

- **Languages & Libraries**: Python, Pandas, NumPy, Scikit-learn, XGBoost, Plotly, Streamlit, Flask
- **ML/AI**: Isolation Forest, XGBoost, LSTM, Prophet, SHAP
- **Visualization**: Plotly, Streamlit, Folium
- **Geospatial**: Geopy, GPS data simulation
- **Fraud Detection**: Graph-based, Isolation Forest (statistical)
- **Others**: Email API, OpenCV, YOLO (optional), Blockchain-ready structure

---

## 🧾 Folder Structure
├── app.py # Flask app (alternative to dashboard) ├── dashboard.py # Streamlit dashboard with 3 main tabs ├── attendance_tracker.py # Tracks teddy warehouse entries ├── delivery_predictor.py # Predicts delivery anomalies ├── delivery_time_prediction.py # Regression model for delay in mins ├── demand_prediction.py # LSTM/Prophet demand forecasting ├── fake_delivery_detection.py # Fraud via delivery timing ├── fake_order_detection.py # Fraud via abnormal amounts/frequency ├── duplicate_order_detected.py # Graph-based duplicate detection ├── customer_preference.py # K-Means clustering on customer order pattern ├── gps_tracker.py # Location-based GPS tracking ├── geofence_tracking.py # Checks teddy inside warehouse or not ├── shap_lime_explainability.py # SHAP/LIME explainability of frauds ├── blockchain_tracking.py # Simulated blockchain for secure delivery log ├── email_templated.py # HTML-based email alerts ├── indoor_tracking.py # Optional BLE tracking logic ├── data_clean.py # Data preprocessing & cleaning ├── templates/ # HTML visual output for dashboard (if Flask used) ├── data/ # Contains teddy_attendance.csv, delivery_tracking.csv, etc.

---

## 📊 Dashboard Preview

![Dashboard Screenshot](Screenshot(605).png)

- **Tab 1**: Attendance log of teddy bears (Present/Absent)
- **Tab 2**: Delivery delays with Plotly histogram
- **Tab 3**: Fraud detection and anomaly logs

---

## 📬 Email Alert Example

HTML-formatted email showing detected fake deliveries and suspicious patterns.

---

## ⚡ How to Run

1. Install dependencies:
```bash
streamlit run dashboard.py

 Run any individual module:
```bash
python delivery_predictor.py
python fraud_detection.py
