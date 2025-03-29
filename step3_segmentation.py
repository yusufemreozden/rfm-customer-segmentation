import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# 1. Veriyi oku
df = pd.read_csv("rfm_data.csv")

# 2. Sadece sayısal RFM kolonlarını seç
rfm = df[["Recency", "Frequency", "Monetary"]]

# 3. Standardize et
scaler = StandardScaler()
rfm_scaled = scaler.fit_transform(rfm)

# 4. KMeans modelini oluştur (k=4)
kmeans = KMeans(n_clusters=4, random_state=42)
df["Segment"] = kmeans.fit_predict(rfm_scaled)

# 5. Segment ortalamalarını görselle
print("\n📊 Segment Analizi:\n")
print(df.groupby("Segment")[["Recency", "Frequency", "Monetary"]].mean().round(2))

# 6. Segmentlenmiş veriyi kaydet
df.to_csv("rfm_segmented.csv", index=False)
print("\n💾 Segmentlenmiş veri 'rfm_segmented.csv' olarak kaydedildi.")
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# 1. Veriyi oku
df = pd.read_csv("rfm_data.csv")

# 2. Sadece sayısal RFM kolonlarını seç
rfm = df[["Recency", "Frequency", "Monetary"]]

# 3. Standardize et
scaler = StandardScaler()
rfm_scaled = scaler.fit_transform(rfm)

# 4. KMeans modelini oluştur (k=4)
kmeans = KMeans(n_clusters=4, random_state=42)
df["Segment"] = kmeans.fit_predict(rfm_scaled)

# 5. Segment ortalamalarını görselle
print("\n📊 Segment Analizi:\n")
print(df.groupby("Segment")[["Recency", "Frequency", "Monetary"]].mean().round(2))

# 6. Segmentlenmiş veriyi kaydet
df.to_csv("rfm_segmented.csv", index=False)
print("\n💾 Segmentlenmiş veri 'rfm_segmented.csv' olarak kaydedildi.")