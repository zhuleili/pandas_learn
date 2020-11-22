import numpy as np  # 快速操作结构数组的工具
import pandas as pd
import matplotlib.pyplot as plt  # 可视化绘制
from sklearn.linear_model import Lasso, LassoCV, LassoLarsCV, Ridge
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
from pandas.core.frame import DataFrame
from sklearn.preprocessing import StandardScaler

newdata = pd.read_excel('D://数据处理//lasso//岭回归和LASSO.xlsx')
# 相关系数查看
# data.corr()

# # 归一化处理
# arr_mean = np.mean(data)  # 求均值
# arr_std = np.std(data, ddof=1)  # 求标准差
# newdata = (data - arr_mean) / arr_std

# 分组抽样划分训练集和测试集
X = newdata[["X1", "X2", "X3", "X4", "X5", "X6", "X7", "X8", "X9", "X10", "X11", "X12", "X13", "X14", "X15", "X16", "X17", "X18", "X19"]]
bb = ["Z1", "Y1", "Z2", "Y2", "Z3", "Y3", "Z4", "Y4"]
result = [("因变量", "成绩", "X1", "X2", "X3", "X4", "X5", "X6", "X7", "X8", "X9", "X10", "X11", "X12", "X13", "X14", "X15",
           "X16", "X17", "X18", "X19")]
for i in bb:
    coef = [i]
    Y = newdata[[i]]
    x_train, x_test, y_train, y_test = train_test_split(X.values, Y.values)

    std_x = StandardScaler()
    x_train = std_x.fit_transform(x_train)
    std_y = StandardScaler()
    y_train = std_y.fit_transform(y_train.reshape(-1, 1))

    lasso = Lasso(alpha=0.1)
    lasso.fit(x_train, y_train)
    coef.append(lasso.score(x_train, y_train))
    for j in lasso.coef_:
        coef.append(j)
    result.append(coef)
    # print(i)
    # print(lasso.score(X_train, y_train))
    # print(lasso.coef_)
    # print("------------------------------")

pd.DataFrame(result).to_excel('D:/数据处理/lasso/result_0.1.xlsx')
print("end")

# lasso005 = Lasso(alpha=0.05).fit(X_train, y_train)
# lasso00001 = Lasso(alpha=0.0001).fit(X_train, y_train)
# lasso05 = Lasso(alpha=0.5).fit(X_train, y_train)

# # print('**********************************')
# # print("Lasso alpha=1")
# # print("training set score:{:.2f}".format(lasso001.score(X_train, y_train)))
# # print("test set score:{:.2f}".format(lasso001.score(X_test, y_test)))
# # print("Number of features used:{}".format(np.sum(lasso001.coef_ != 0)))
#
# # 建立岭回归实例
# ridge01 = Ridge(alpha=0.01).fit(X_train, y_train)
#
# # 计算R方
# ridge01.score(X_train, y_train)
#
# # 打印整个模型
# # print("住院天数 = " + str(a.intercept_[0]) + " + " + str(a.coef_[0][0]) + " * CRIM")
#
# # 进行预测和比较
# output = ridge01.predict(X_test)
# output1 = DataFrame(output)
#
# outputdata = pd.concat([output1, y_test])  # 直接合并数据框
# outputdata.to_csv('D://数据处理//lasso//result.csv', index=False)
