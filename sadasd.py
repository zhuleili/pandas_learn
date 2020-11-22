# 导入第三方包
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
# % matplotlib inline
from pandas import Series, DataFrame
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge, RidgeCV
from sklearn.linear_model import Lasso, LassoCV
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
from sklearn.preprocessing import StandardScaler

df = pd.read_csv('data0804.csv')

df[['X18', 'X19']] = pd.get_dummies(df[['X18', 'X19']])  # 哑变量处理
YY = ['Y1', 'Z1', 'Y2', 'Z2', 'Y3', 'Z3', 'Y4', 'Z4']
XX = ['X1', 'X2', 'X3', 'X4', 'X5', 'X6', 'X7', 'X8', 'X9', 'X10', 'X11', 'X12', 'X13', 'X14', 'X15', 'X16', 'X17',
      'X18', 'X19']

all_score = []
all_RMSE = []
for j in range(1000):
    X_train, X_test, y_train, y_test = train_test_split(df[XX].values, df['Y1'].values, train_size=0.75, random_state=j)

    alphas = 10 ** np.linspace(-3, 3, 100)
    lasso_cofficients = []
    for alpha in alphas:
        lasso = Lasso(alpha=alpha, normalize=True, max_iter=10000)
        lasso.fit(X_train, y_train)
        lasso_cofficients.append(lasso.coef_)

    lasso_cv = LassoCV(alphas=alphas, normalize=True, cv=3, max_iter=10000)
    lasso_cv.fit(X_train, y_train)
    # 取出最佳的lambda值
    lasso_best_alpha = lasso_cv.alpha_

    # 基于最佳的lambda值建模
    lasso = Lasso(alpha=lasso_best_alpha, normalize=True, max_iter=10000)
    lasso.fit(X_train, y_train)
    # 岭回归系数
    # coef_arr.append(lasso.coef_)
    # intercept_arr.append(lasso.intercept_)

    # 预测
    lasso_predict = lasso.predict(X_test)

    # # 预测效果验证
    RMSE = np.sqrt(mean_squared_error(y_test, lasso_predict))

    score = r2_score(y_test, lasso_predict)
    # print(j)
    # print(RMSE)
    # print(score)
    all_RMSE.append(RMSE)
    all_score.append(score)
    # print(lasso.coef_)
    # print(lasso.intercept_)
    print("this time random_state=%s" % j)
print("all_RMSE")
print(all_RMSE)

print("------------------")
print("all_score")
print(all_score)
print("max-score=%s" % max(all_score))
print("good_random_state=%s" % all_score.index(max(all_score)))