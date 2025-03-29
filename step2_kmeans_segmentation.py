import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# data loading
df = pd.read_csv("rfm_data.csv")

# normalizasyon
scaler = StandardScaler()
scaled_rfm = scaler.fit_transform(df[["Recency", "Frequency", "Monetary"]])

# elbow
sse = []
k_range = range(1, 11)
for k in k_range:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(scaled_rfm)
    sse.append(kmeans.inertia_)

# graph
plt.figure(figsize=(8, 5))
plt.plot(k_range, sse, marker='o')
plt.xlabel("Number of Clusters (k)")
plt.ylabel("SSE (Inertia)")
plt.title("Elbow Method for Optimal k")
plt.grid(True)
plt.tight_layout()
plt.savefig("elbow_plot.png")
plt.show()
