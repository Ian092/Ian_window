import pandas as pd
import matplotlib.pyplot as plt

# 讀取 CSV 檔案
file_path = '統計表.csv'
data = pd.read_csv(file_path)

# 檢查數據列
print(data.columns)

# 繪製「長照機構數」欄位的箱形圖
column_name = '長照機構數%'

fig = plt.figure()
ax = fig.add_subplot(111)

# Create box plot
box = ax.boxplot(data[column_name], patch_artist=True, showmeans=True)

# 設定標題和標籤 (以日文表示，根據上圖的需求)
ax.set_title('長照機構數%')

# 自訂箱形圖
for median in box['medians']:
    median.set(color='orange', linewidth=1.5)
for mean in box['means']:
    mean.set(marker='^', color='green', markersize=10)

plt.show()
