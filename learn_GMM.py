from sklearn.mixture import GaussianMixture
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

before = GaussianMixture(n_components=4)  # 降维前
before.fit(loan)
print('GMM降维前-分类结果')
# print(before.labels_)

# 归一化 准备降维
X_norm = StandardScaler().fit_transform(loan)
X_norm.mean(axis=0)      # 每一维均值为0

# 准备可视化需要的降维数据 降到2维  默认2维
data_TSNE = TSNE().fit_transform(X_norm)

after = GaussianMixture(n_components=4)  # 降维后
after.fit(data_TSNE)
print('GMM降维后-分类结果')
# print(after.labels_)

nowTime = time.strftime("%Y%m%d%H%M%S", time.localtime())
save_path = 'D:/数据处理/GMM分类出图%s/' % nowTime
os.makedirs(save_path)

# 手肘法 '利用SSE选择k' 即聚类个数
# SSE = []  # 存放每次结果的误差平方和
# for k in range(2, 8):
#     estimator = GaussianMixture(n_components=k)  # 构造聚类器
#     estimator.fit(data_TSNE)
#     SSE.append(estimator.precisions_.max)  # 存放每次结果的误差平方和
# X = range(2, 8)
# plt.xlabel('GMM-k')
# plt.ylabel('GMM-SSE')
# plt.plot(X, SSE, 'o-')
# plt.savefig('%sSSE.png' % save_path)
# plt.show()

'''对不同的k进行试探性GMM聚类并可视化'''
for i in range(2, 8):
    gmm = GaussianMixture(n_components=i).fit_predict(data_TSNE)
    colors = ([['red', 'blue', 'black', 'green', 'yellow', 'orange', 'purple'][i] for i in gmm])
    plt.rc('font', family='STXihei', size=10)
    plt.scatter(data_TSNE[:, 0], data_TSNE[:, 1], c=colors, s=100)
    plt.title('GMM分%s类' % str(i))
    plt.savefig('%s分%s类.png' % (save_path, str(i)))
    plt.show()


