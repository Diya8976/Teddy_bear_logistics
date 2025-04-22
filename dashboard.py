import streamlit as st
import pandas as pd
import plotly.express as px
import os


os.system("python fake_delivery_detection.py")

st.title("🧸 Teddy Bear AI Logistics Dashboard")

tab1, tab2, tab3 = st.tabs(["📋 Attendance", "🚚 Deliveries", "🚨 Fraud Detection"])

with tab1:
    df = pd.read_csv("teddy_attendance.csv")
    st.subheader("Teddy Bear Attendance Log")
    st.dataframe(df.tail(10))

with tab2:
    df = pd.read_csv("delivery_tracking.csv")
    df["actual_delivery"] = pd.to_datetime(df["actual_delivery"])
    df["expected_delivery"] = pd.to_datetime(df["expected_delivery"])
    df["delay"] = (df["actual_delivery"] - df["expected_delivery"]).dt.total_seconds() / 60
    fig = px.histogram(df, x="delay", nbins=20, title="Delivery Delay Distribution")
    st.plotly_chart(fig)
    st.dataframe(df.tail(10))

with tab3:
    df = pd.read_csv("fraud_logs.csv")
    st.subheader("Detected Fraud Entries")
    st.dataframe(df)
