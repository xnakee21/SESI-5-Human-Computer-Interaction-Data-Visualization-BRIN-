import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# 1. Dataset Penjualan Multi-Kategori
data_vis = {
    'Bulan': ['Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Jun'],
    'Elektronik': [120, 140, 135, 170, 195, 210],
    'Pakaian': [80, 95, 110, 105, 130, 150],
    'Makanan': [200, 210, 205, 220, 240, 250]
}
df_vis = pd.DataFrame(data_vis)

# 2. Pengaturan Layout Dashboard Visualisasi (2 Subplot)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
sns.set_theme(style="white") # Memangkas Chartjunk (Background Kertas Bersih)

# Subplot 1: Line Chart Tren Penjualan (Overview First)
ax1.plot(df_vis['Bulan'], df_vis['Elektronik'], marker='o', linewidth=2.5, label='Elektronik', color='#1f77b4')
ax1.plot(df_vis['Bulan'], df_vis['Pakaian'], marker='s', linewidth=2.5, label='Pakaian', color='#ff7f0e')
ax1.plot(df_vis['Bulan'], df_vis['Makanan'], marker='^', linewidth=2.5, label='Makanan', color='#2ca02c')

ax1.set_title('Tren Penjualan per Kategori (Semester I 2026)', fontsize=12, fontweight='bold', pad=12)
ax1.set_ylabel('Total Penjualan (Juta Rp)')
ax1.legend(frameon=False) # Menghapus bingkai legenda
sns.despine(ax=ax1) # Menghapus border atas dan kanan

# Subplot 2: Bar Chart Kontribusi Total Penjualan
total_per_kategori = {
    'Elektronik': df_vis['Elektronik'].sum(),
    'Pakaian': df_vis['Pakaian'].sum(),
    'Makanan': df_vis['Makanan'].sum()
}

ax2.bar(total_per_kategori.keys(), total_per_kategori.values(), color=['#1f77b4', '#ff7f0e', '#2ca02c'], width=0.5)
ax2.set_title('Total Kontribusi Penjualan per Kategori', fontsize=12, fontweight='bold', pad=12)
ax2.set_ylabel('Total Kumulatif (Juta Rp)')
sns.despine(ax=ax2)

# Menambahkan Angka Detail di Atas Bar (Details on Demand)
for k, v in total_per_kategori.items():
    ax2.text(k, v + 20, f"{v} Juta", ha='center', fontsize=10, fontweight='bold')

plt.tight_layout()
plt.show()
