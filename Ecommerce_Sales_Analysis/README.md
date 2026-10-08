# 📊 Superstore Sales Analysis & Dashboard (EDA)

This project performs data cleaning, sales summary calculations, and localized sales performance visualization using Python. It identifies total performance metrics and highlights the top-performing locations based on shipping postal codes.

## 🚀 Project Features
* **Data Preprocessing:** Drops unnecessary columns (like `Row ID`), standardizes `Postal Code` data formats to text strings, and removes missing fields.
* **Key Metrics Extracted:** Calculates total sales revenue and average order value.
* **Top Performance Insights:** Identifies the top 10 retail locations (Postal Codes) sorted by total generated sales.
* **Data Visualization:** Generates a custom styled Seaborn bar chart dashboard showcasing top-performing locations.

## 📊 Sample Visual Output
When executed, the script outputs data logs to the console and renders a geographical bar plot dashboard:

* **Total Sales Revenue Analysis:** Calculated dynamically across the entire store matrix.
* **Location Performance:** Displays a clear bar chart of the highest revenue-generating postal codes.

---

## 🛠️ Setup & Execution Guide

1. **Clone the repository to your machine:**
   ```bash
   git clone https://github.com
   cd superstore-sales-eda
   ```

2. **Install the required libraries:**
   ```bash
   pip install pandas matplotlib seaborn
   ```

3. **Execute the Python analysis script:**
   ```bash
   python sales_analysis.py
   ```

## ⚙️ Technologies Used
* **Python** (Core computational logic)
* **Pandas** (Data cleaning & aggregations)
* **Matplotlib & Seaborn** (Data visualization & plotting)
