import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

df = pd.read_csv("rfm_data.csv")

# sayısal RFM kolonlarını seçme
rfm = df[["Recency", "Frequency", "Monetary"]]

# standardize
scaler = StandardScaler()
rfm_scaled = scaler.fit_transform(rfm)

# KMeans model (k=4)
kmeans = KMeans(n_clusters=4, random_state=42)
df["Segment"] = kmeans.fit_predict(rfm_scaled)

# ortalamaların görseli
print("\n📊 Segment Analizi:\n")
print(df.groupby("Segment")[["Recency", "Frequency", "Monetary"]].mean().round(2))

# segmented datayı kaydet
df.to_csv("rfm_segmented.csv", index=False)
print("\n💾 Segmentlenmiş veri 'rfm_segmented.csv' olarak kaydedildi.")
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# read to data
df = pd.read_csv("rfm_data.csv")

# sadece sayısal RFM kolonlarını seç
rfm = df[["Recency", "Frequency", "Monetary"]]

# standardize et
scaler = StandardScaler()
rfm_scaled = scaler.fit_transform(rfm)

# KMeans modelini oluştur (k=4)
kmeans = KMeans(n_clusters=4, random_state=42)
df["Segment"] = kmeans.fit_predict(rfm_scaled)

# segment ortalamalarını görselle
print("\n📊 Segment Analizi:\n")
print(df.groupby("Segment")[["Recency", "Frequency", "Monetary"]].mean().round(2))

# segmentlenmişleri kaydet
df.to_csv("rfm_segmented.csv", index=False)
print("\n💾 Segmentlenmiş veri 'rfm_segmented.csv' olarak kaydedildi.")
