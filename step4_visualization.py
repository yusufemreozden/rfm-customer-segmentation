import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# === Segmentlenmiş veriyi yükle
df = pd.read_csv("rfm_segmented.csv")

# === Görsel stili ayarla
sns.set(style="whitegrid")

# === 2D Scatter Plot (Recency vs Monetary, renk = Segment)
plt.figure(figsize=(10, 6))
sns.scatterplot(
    data=df,
    x="Recency",
    y="Monetary",
    hue="Segment",
    palette="Set2",
    s=100,
    alpha=0.8
)
plt.title("RFM Müşteri Segmentasyonu (Recency vs Monetary)", fontsize=14)
plt.xlabel("Recency (Son Alışveriş Gün Sayısı)")
plt.ylabel("Monetary (Toplam Harcama)")
plt.legend(title="Segment")
plt.tight_layout()
plt.savefig("segment_plot.png")
plt.show()
