# dashboard.py

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load your cleaned dataset
df = pd.read_csv("Preprocessed.csv", parse_dates=["Order Date"])

st.title("🛍️ Sales Data Dashboard")

# Sidebar filters
city = st.sidebar.selectbox("Select City", options=df["City"].unique())
month = st.sidebar.selectbox("Select Month", options=sorted(df["Month"].unique()))

filtered_df = df[(df["City"] == city) & (df["Month"] == month)]

# Top Products
st.subheader(f"Top Products in {city} (Month: {month})")
top_products = filtered_df["Product"].value_counts().head(5)
st.bar_chart(top_products)

# Hourly Order Volume
st.subheader("Hourly Orders")
hourly = filtered_df["Hour"].value_counts().sort_index()
st.line_chart(hourly)

# Sales Summary
st.subheader("Total Sales")
st.metric(label="Total Sales", value=f"${filtered_df['Sales'].sum():,.2f}")

# Daily Sales Trend
st.subheader("Sales Trend Over Month")
daily_sales = filtered_df.groupby("Order Date")["Sales"].sum()
st.line_chart(daily_sales)
