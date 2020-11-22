import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# index_col=0 取第一列作为索引
data = pd.read_excel('D:\数据处理\源数据\热力图(2).xlsx', index_col=0)

# 行列转换
new_data = pd.DataFrame(data).stack().unstack(0)
sns.heatmap(new_data, cmap='Reds')
plt.show()

