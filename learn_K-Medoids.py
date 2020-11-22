from pyclust import KMedoids
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.manifold import TSNE
import time
import os
from sklearn.preprocessing import StandardScaler

loan_data = pd.read_excel("C:\\Users\\Administrator\\Desktop\\all_(1h)(1).xlsx",
                          sheet_name="test", header=0, names=None, index_col=0)
# 设置要进行聚类的字段
loan = np.array(loan_data[['INA5', 'INA15', 'INP5', 'INP15', 'OUTA5', 'OUTA15', 'OUTP5', 'OUTP15']])

before = KMedoids(n_clusters=4)  # 降维前
before.fit(loan)
print('KMedoids降维前-分类结果')
print(before.labels_)

# 归一化 准备降维
X_norm = StandardScaler().fit_transform(loan)
X_norm.mean(axis=0)      # 每一维均值为0

# 降维法1:------------------------------
# 求特征值和特征向量
ew, ev = np.linalg.eig(np.cov(X_norm.T))   # np.cov直接求协方差矩阵，每一行代表一个特征，每一轮代表样本

# 特征向量特征值的排序
ew_oreder = np.argsort(ew)[::-1]
ew_sort = ew[ew_oreder]
ev_sort = ev[:, ew_oreder]  # ev的每一列代表一个特征向量
ev_sort.shape  # (4,4)

# 我们指定降成2维， 然后取出排序后的特征向量的前两列就是基
K = 2
V = ev_sort[:, :2]  # 4*2

# 最后，我们得到降维后的数据
X_new = X_norm.dot(V)    # shape (150,2)
# ------------------------------

# # 降维法2:准备可视化需要的降维数据 降到2维  默认2维
# X_new = TSNE().fit_transform(X_norm)

after = KMedoids(n_clusters=4)  # 降维后
after.fit(X_new)
print('KMedoids降维后-分类结果')
print(after.labels_)

nowTime = time.strftime("%Y%m%d%H%M%S", time.localtime())
save_path = 'D:/数据处理/KMedoids分类出图%s/' % nowTime
os.makedirs(save_path)

# 手肘法 '利用SSE选择k' 即聚类个数
SSE = []  # 存放每次结果的误差平方和
for k in range(2, 8):
    estimator = KMedoids(n_clusters=k)  # 构造聚类器
    estimator.fit(loan)
    SSE.append(estimator.sse_arr_[0] + estimator.sse_arr_[1])  # 存放每次结果的误差平方和
X = range(2, 8)
plt.xlabel('KMedoids-k')
plt.ylabel('KMedoids-SSE')
plt.plot(X, SSE, 'o-')
plt.savefig('%sSSE.png' % save_path)
plt.show()

'''对不同的k进行试探性K-medoids聚类并可视化'''
for i in range(2, 8):
    k = KMedoids(n_clusters=i, distance='euclidean', max_iter=1000).fit_predict(X_new)
    colors = ([['red', 'blue', 'black', 'green', 'yellow', 'orange', 'purple'][i] for i in k])
    plt.rc('font', family='STXihei', size=10)
    plt.scatter(X_new[:, 0], X_new[:, 1], c=colors, s=100)
    plt.title('KMedoids分%s类' % str(i))
    plt.savefig('%s分%s类.png' % (save_path, str(i)))
    plt.show()
