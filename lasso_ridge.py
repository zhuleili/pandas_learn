# 导入第三方包
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas import DataFrame
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge, RidgeCV
from sklearn.linear_model import Lasso, LassoCV
from sklearn.metrics import mean_squared_error

df = pd.read_csv('D://数据处理//源数据//EPHF20200727.csv')


df[['X18', 'X19']] = pd.get_dummies(df[['X18', 'X19']])  # 哑变量处理
YY = ['Y1', 'Z1', 'Y2', 'Z2', 'Y3', 'Z3', 'Y4', 'Z4']
XX = ['X1', 'X2', 'X3', 'X4', 'X5', 'X6', 'X7', 'X8', 'X9', 'X10', 'X11', 'X12', 'X13', 'X14', 'X15', 'X16', 'X17',
      'X18', 'X19']
ridge_best_alpha_arr = []
coef_arr = []
intercept_arr = []
RMSE_ARR = []
ridge_predict_arr = []

# for i in YY:
#     X_train, X_test, y_train, y_test = train_test_split(df[XX].values, df[i].values, train_size=0.8, random_state=1234)
#
#     # 通过不确定的alphas值，生成不同的岭回归模型
#     alphas = 10 ** np.linspace(-3, 3, 100)
#     ridge_cofficients = []
#     for alpha in alphas:
#         ridge = Ridge(alpha=alpha, normalize=True)
#         ridge.fit(X_train, y_train)
#         ridge_cofficients.append(ridge.coef_)
#
#     # 绘制alpha的对数与回归系数的关系
#     # 中文乱码和坐标轴负号的处理
#     #     plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
#     #     plt.rcParams['axes.unicode_minus'] = False
#
#     #     # 设置绘图风格
#     #     plt.style.use('ggplot')
#     #     plt.plot(alphas, ridge_cofficients)
#     #     plt.xscale('log')
#     #     plt.axis('tight')
#     #     plt.title('alpha系数与岭回归系数的关系')
#     #     plt.xlabel('Log Alpha')
#     #     plt.ylabel('Cofficients')
#     #     plt.show()
#
#     # 为了找到最佳的lambda值，我们采用交叉验证方法
#     # 岭回归模型的交叉验证
#     ridge_cv = RidgeCV(alphas=alphas, normalize=True, scoring='neg_mean_squared_error', cv=5)
#     ridge_cv.fit(X_train, y_train)
#     # 取出最佳的lambda值
#     ridge_best_alpha = ridge_cv.alpha_
#     ridge_best_alpha_arr.append(ridge_best_alpha)
#
#     # 基于最佳的lambda值建模
#     ridge = Ridge(alpha=ridge_best_alpha, normalize=True)
#     ridge.fit(X_train, y_train)
#     # 岭回归系数
#     coef_arr.append(ridge.coef_)
#     intercept_arr.append(ridge.intercept_)
#
#     # 预测
#     ridge_predict = ridge.predict(df[XX])
#     ridge_predict_arr.append(ridge_predict)
#
#     # 预测效果验证
# #     RMSE = np.sqrt(mean_squared_error(y_test,ridge_predict))
# #     RMSE_ARR.append(RMSE)
# print(ridge_best_alpha_arr)
# print(coef_arr)
# print(intercept_arr)
# print(ridge_predict_arr)
# print(RMSE_ARR)
#
# predicts = DataFrame(ridge_predict_arr).stack().unstack(0)  # 行列转换
# print(predicts)
#
# predicts['Z1*Y1'] = predicts[0].mul(predicts[1]).mul(df['A1_line'])
# predicts['Z2*Y2'] = predicts[2].mul(predicts[3]).mul(df['A2_line'])
# predicts['Z3*Y3'] = predicts[4].mul(predicts[5]).mul(df['P1_line'])
# predicts['Z4*Y4'] = predicts[6].mul(predicts[7]).mul(df['P2_line'])
#
# predicts['Z1*Y1/station'] = (predicts['Z1*Y1'].sub(df['A1_station'])).abs().div(df['A1_station'])
# predicts['Z2*Y2/station'] = (predicts['Z2*Y2'].sub(df['A2_station'])).abs().div(df['A2_station'])
# predicts['Z3*Y3/station'] = (predicts['Z3*Y3'].sub(df['P1_station'])).abs().div(df['P1_station'])
# predicts['Z4*Y4/station'] = (predicts['Z4*Y4'].sub(df['P2_station'])).abs().div(df['P2_station'])
#
# predicts.to_excel('D:/数据处理/lasso/岭回归_resul.xlsx')



# # Plot the results
# m1 = plt.scatter(366 * X_train, y_train, color=cmap(0.9), s=10)
# m2 = plt.scatter(366 * X_test, y_test, color=cmap(0.5), s=10)
# plt.plot(366 * X, y_pred_line, color='black', linewidth=2, label="Prediction")
# plt.suptitle("Lasso Regression")
# plt.title("MSE: %.2f" % mse, fontsize=10)
# plt.xlabel('Day')
# plt.ylabel('Temperature in Celcius')
# plt.legend((m1, m2), ("Training data", "Test data"), loc='lower right')
# plt.show()

coef_result = []
for i in YY:
    result = []
    # X_train, X_test, y_train, y_test = train_test_split(df[XX].values, df[i].values, train_size=1, random_state=1234)
    # 通过不确定的alphas值，生成不同的LASSO回归模型
    alphas = 10 ** np.linspace(-3, 3, 100)
    lasso_cofficients = []
    for alpha in alphas:
        lasso = Lasso(alpha=alpha, normalize=True, max_iter=10000)
        lasso.fit(df[XX].values, df[i].values)
        lasso_cofficients.append(lasso.coef_)

    # 绘制alpha的对数与回归系数的关系
    # 中文乱码和坐标轴负号的处理
    plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
    plt.rcParams['axes.unicode_minus'] = False

    # 设置绘图风格
    # plt.style.use('ggplot')
    # plt.plot(alphas, lasso_cofficients)
    # plt.xscale('log')
    # plt.axis('tight')
    # plt.title('alpha系数与LASSO回归系数的关系')
    # plt.xlabel('Log Alpha')
    # plt.ylabel('Cofficients')
    # plt.show()

    # LASSO回归模型的交叉验证
    lasso_cv = LassoCV(alphas=alphas, normalize=True, cv=3, max_iter=10000)
    lasso_cv.fit(df[XX].values, df[i].values)
    # 取出最佳的lambda值
    lasso_best_alpha = lasso_cv.alpha_
    ridge_best_alpha_arr.append(lasso_best_alpha)

    # 基于最佳的lambda值建模
    lasso = Lasso(alpha=lasso_best_alpha, normalize=True, max_iter=10000)
    lasso.fit(df[XX].values, df[i].values)
    # 岭回归系数
    coef_arr.append(lasso.coef_)
    intercept_arr.append(lasso.intercept_)

    result.append(lasso_best_alpha)
    result.extend(lasso.coef_)
    # 预测
    # lasso_predict = lasso.predict(df[XX])
    # ridge_predict_arr.append(lasso_predict)

    # # 预测效果验证
    # RMSE = np.sqrt(mean_squared_error(y_test, lasso_predict))
    # RMSE_ARR.append(RMSE)

    coef_result.append(result)
# print(ridge_best_alpha_arr)
# print(coef_arr)
# print(intercept_arr)
# print(ridge_predict_arr)
# print(RMSE_ARR)
DataFrame(intercept_arr).to_excel('D:/数据处理/lasso/intercept_result_all.xlsx')
DataFrame(coef_result).to_excel('D:/数据处理/lasso/coef_result_all.xlsx')




# predicts = DataFrame(ridge_predict_arr).stack().unstack(0)  # 行列转换
# print(predicts)
#
# predicts['Z1*Y1'] = predicts[0].mul(predicts[1]).mul(df['A1_line'])
# predicts['Z2*Y2'] = predicts[2].mul(predicts[3]).mul(df['A2_line'])
# predicts['Z3*Y3'] = predicts[4].mul(predicts[5]).mul(df['P1_line'])
# predicts['Z4*Y4'] = predicts[6].mul(predicts[7]).mul(df['P2_line'])
#
# predicts['Z1*Y1/station'] = (predicts['Z1*Y1'].sub(df['A1_station'])).abs().div(df['A1_station'])
# predicts['Z2*Y2/station'] = (predicts['Z2*Y2'].sub(df['A2_station'])).abs().div(df['A2_station'])
# predicts['Z3*Y3/station'] = (predicts['Z3*Y3'].sub(df['P1_station'])).abs().div(df['P1_station'])
# predicts['Z4*Y4/station'] = (predicts['Z4*Y4'].sub(df['P2_station'])).abs().div(df['P2_station'])

# DataFrame(coef_result).to_excel('D:/数据处理/lasso/coef_result.xlsx')
