import pandas as pd

# Veriyi oku
df = pd.read_csv("rfm_data.csv")

# Genel bilgiler
print("✅ Veri seti boyutu:", df.shape)
print("\n📌 İlk 5 Satır:\n", df.head())
print("\n🔎 Veri Tipleri:\n", df.dtypes)
print("\n📊 Temel İstatistikler:\n", df.describe())