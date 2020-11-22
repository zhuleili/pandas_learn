import numpy as np

import matplotlib.pyplot as plt

import pandas as pd
df = pd.read_csv('D:\数据处理\源数据\data0806.csv')
df[['X18', 'X19']] = pd.get_dummies(df[['X19', 'X20']])  # 哑变量处理

XX = ['X1', 'X2', 'X3', 'X4', 'X5', 'X6', 'X7', 'X8', 'X9', 'X10', 'X11', 'X12', 'X13', 'X14', 'X15', 'X16', 'X17',
      'X18', 'X19','X20']
# YY = ['Z1']

from sklearn.feature_selection import RFE
from sklearn.linear_model import LinearRegression
lr = LinearRegression()
rfe = RFE(lr, n_features_to_select=3)
rfe.fit(df[XX], df['Z1'])
var = rfe.get_support(True)
print(var)