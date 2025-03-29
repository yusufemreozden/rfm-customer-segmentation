# 📊 RFM Customer Segmentation

A complete data science project using **RFM analysis** and **KMeans clustering** to segment telecom customers based on behavior.  
Includes data preprocessing, clustering, visualization, and a PDF business report with segment-based strategies.

---

## 🚀 Project Overview

- 🎯 **Goal**: Segment customers based on Recency, Frequency, and Monetary value (RFM)
- 🧠 **Methods**: RFM Analysis, K-Means Clustering, StandardScaler
- 📊 **Dataset**: 1,000 synthetic customers with Recency, Frequency, and Monetary metrics
- 🛠️ **Tools**: Python, Pandas, Scikit-learn, Matplotlib, Seaborn

---

## 🔁 RFM Metrics

- **Recency (R)** – Days since last purchase
- **Frequency (F)** – Total number of purchases
- **Monetary (M)** – Total amount spent

---

## 🧱 Project Pipeline

1. **📥 Data Loading & Exploration**
   - Dataset shape and structure
   - Summary statistics and data types

2. **🧹 Preprocessing**
   - Feature scaling using `StandardScaler`
   - Visualizing optimal `k` with Elbow Method

3. **🔍 Clustering**
   - KMeans clustering with optimal `k`
   - Segment-level aggregation and analysis

4. **📊 Visualization**
   - Customer clusters (Recency vs Monetary)
   - Save segment results as CSV

5. **📄 Reporting**
   - Business interpretation of each segment
   - Marketing strategy suggestions per segment

---

## 🧾 Sample Output

| Segment | Recency | Frequency | Monetary |
|---------|---------|-----------|----------|
| 0       | 222.87  | 14.54     | 392.81   |
| 1       |  93.05  |  6.03     | 490.53   |
| 2       | 269.16  |  5.48     | 969.15   |
| 3       | 142.55  | 14.18     | 1117.77  |

---

## 📄 Report

Final insights and segment descriptions are summarized in this business report:

👉 [📎 View Segmentation Report (PDF)](./rfm_segmentation_report.pdf)

---

## ✨ Future Improvements

- Test different clustering algorithms (DBSCAN, Agglomerative)
- Use RFM percentiles for smarter bucketing
- Add more features like region, age, or product type
- Deploy on Streamlit for interactive analysis

---

## 🔐 License

This project is licensed under the [MIT License](LICENSE).
