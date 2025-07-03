# 🛒 Sales Data Analysis and Dashboard (EDA + Streamlit)

## 📌 Overview

This project focuses on performing **Exploratory Data Analysis (EDA)** and building a simple **interactive dashboard** on sales data collected from multiple CSV files. It aims to extract key insights on product performance, customer behavior, and geographic trends across cities in the U.S.

Though marked as "incomplete", the work completed covers full data cleaning, feature engineering, visualization, and dashboard development — making it a great learning milestone.

---

## 🧠 Objectives

- 📂 Combine monthly sales data stored in multiple CSV files.
- 🧹 Clean and preprocess the data (remove NaNs, incorrect rows).
- 🏷️ Create new meaningful columns (e.g., `Sales`, `Month`, `City`, `Time`, `ZIP`).
- 📊 Visualize patterns through multiple graphs (sales trends, product popularity, hourly patterns, etc.).
- 🌍 Perform geo-based EDA (sales by city, state).
- 🧮 Generate a heatmap for numeric correlation.
- 🖥️ Build an interactive dashboard using **Streamlit**.

---

## 📁 Project Structure

```
📦 sales-data-analysis/
 ┣ 📂 data/
 ┃ ┣ sales_april.csv
 ┃ ┣ sales_may.csv
 ┃ ┗ ... (multiple monthly CSV files)
 ┣ 📜 analysis.ipynb           # EDA with visualizations
 ┣ 📜 dashboard.py             # Streamlit dashboard code
 ┣ 📜 README.md                # This file

```


## 📊 Key Features Extracted

- **Order Date breakdown** → Month, Day, Hour
- **Location breakdown** → Street Address, City, State, ZIP Code
- **Sales amount** → Quantity × Price
- **Time** → Order time extracted from datetime
- Cleaned columns for final analysis (`Purchased Address` and `Zip Code` were dropped after extraction)

---

## 📈 Visualizations Created

- Product distribution counts
- Top 5 products by city
- Monthly sales trends per city
- Hourly order patterns by city
- Total quantity ordered by product
- Heatmap of numeric correlations
- Line plot for order counts by hour (overall)

---

## 🚀 Dashboard

A `Streamlit` dashboard was built for basic interaction. It works independently from the notebook.

To run the dashboard:
```bash
streamlit run dashboard.py
```

---

## 🎓 What I Learned

- How to work with **multiple CSV files** programmatically.
- Advanced `pandas` manipulation, including `str.split()`, `dt` accessors, and grouping.
- **Data visualization** using `matplotlib` and `seaborn`.
- How to clean, structure, and engineer features from messy raw data.
- Built and launched a **Streamlit dashboard**.
- Practiced a real-life data project workflow end-to-end.

---

## ✅ Next Steps (Future Improvements)

- Add product category analysis
- Include customer behavior insights (repeat orders, popular times)
- Add filters to Streamlit dashboard (by city, product)
- Connect with Excel for additional reporting

---

## 🧩 Status

This project is being marked as **"incomplete but complete enough"**. It serves as a learning checkpoint before shifting to Excel studies. It showcases my ability to:

- Handle real-world datasets
- Perform data cleaning & transformation
- Visualize insights
- Deploy basic dashboards

---

## 📚 Tools Used

- Python 3.10+
- pandas
- matplotlib
- seaborn
- Streamlit

---

