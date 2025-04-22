import pandas as pd

# Create a sample DataFrame for delivery_updates.csv
data = {
    'order_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'order_amount': [100, 150, 200, 50, 300, 120, 180, 250, 220, 130],
    'delivery_status_code': [1, 2, 3, 1, 2, 3, 1, 2, 1, 3]
}

df_orders = pd.DataFrame(data)
df_orders.to_csv('delivery_updates.csv', index=False)

# Create teddy_attendance.csv
attendance_data = {
    'teddy_id': [1, 2, 3, 4, 5],
    'attendance_time': ['2025-04-01 08:00:00', '2025-04-01 08:05:00', '2025-04-01 08:10:00', '2025-04-01 08:15:00', '2025-04-01 08:20:00'],
    'status': ['Present', 'Absent', 'Present', 'Present', 'Present']
}

attendance_df = pd.DataFrame(attendance_data)
attendance_df.to_csv('teddy_attendance.csv', index=False)

# Create delivery_tracking.csv
delivery_data = {
    'teddy_id': [1, 2, 3, 4, 5],
    'vehicle_id': [101, 102, 103, 104, 105],
    'expected_delivery': ['2025-04-01 10:00:00', '2025-04-01 11:00:00', '2025-04-01 12:00:00', '2025-04-01 13:00:00', '2025-04-01 14:00:00'],
    'actual_delivery': ['2025-04-01 10:30:00', '2025-04-01 11:10:00', '2025-04-01 12:05:00', '2025-04-01 13:20:00', '2025-04-01 14:30:00'],
    'start_time': ['2025-04-01 09:30:00', '2025-04-01 10:30:00', '2025-04-01 11:30:00', '2025-04-01 12:30:00', '2025-04-01 13:30:00']  # Added `start_time`
}

delivery_df = pd.DataFrame(delivery_data)
delivery_df.to_csv('delivery_tracking.csv', index=False)

# Create fraud_logs.csv
fraud_data = {
    'order_id': [1001, 1002, 1003, 1004, 1005],
    'customer_id': [101, 102, 101, 104, 103],
    'order_amount': [100, 150, 100, 180, 220],
    'fraud_flag': ['No', 'Yes', 'No', 'No', 'Yes']
}

fraud_df = pd.DataFrame(fraud_data)
fraud_df.to_csv('fraud_logs.csv', index=False)

# Now, let's create the Streamlit app code:

import streamlit as st
import plotly.express as px

st.title("🧸 Teddy Bear AI Logistics Dashboard")

tab1, tab2, tab3 = st.tabs(["📋 Attendance", "🚚 Deliveries", "🚨 Fraud Detection"])

# Tab 1 - Attendance
with tab1:
    df = pd.read_csv("teddy_attendance.csv")
    st.subheader("Teddy Bear Attendance Log")
    st.dataframe(df.tail(10))

# Tab 2 - Deliveries
with tab2:
    df = pd.read_csv("delivery_tracking.csv")
    df["actual_delivery"] = pd.to_datetime(df["actual_delivery"])
    df["expected_delivery"] = pd.to_datetime(df["expected_delivery"])
    df["delay"] = (df["actual_delivery"] - df["expected_delivery"]).dt.total_seconds() / 60  # Calculate delay in minutes
    fig = px.histogram(df, x="delay", nbins=20, title="Delivery Delay Distribution")  # Plot delivery delay distribution
    st.plotly_chart(fig)
    st.dataframe(df.tail(10))

# Tab 3 - Fraud Detection
with tab3:
    df = pd.read_csv("fraud_logs.csv")
    st.subheader("Detected Fraud Entries")
    st.dataframe(df)
