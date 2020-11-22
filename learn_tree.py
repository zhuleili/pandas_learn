from sklearn import tree
import pandas as pd
import numpy as np
import graphviz
import pydot

import os

os.environ['PATH'] = os.environ['PATH'] + (';c:\\Program Files (x86)\\Graphviz2.38\\bin\\')

from sklearn.model_selection import train_test_split

loan_data = pd.read_excel("D:\\数据处理\\源数据\\超高峰小时高峰.xlsx",
                          sheet_name="原超高峰系数+用地数据", header=0, names=None)

x = np.array(loan_data[['效率', '介数', '办公', '中小学', '大学', '商业', '休闲', '医疗', '居住', '交通枢纽', '待开发面积', '距离', '混合用地熵']])
y = np.array(loan_data['kmeans5类'])

# 拆分训练数据与测试数据
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)

# 核心代码：使用信息熵作为划分标准，对决策树进行训练
clf = tree.DecisionTreeClassifier(criterion='entropy')
clf.fit(x_train, y_train)
score = clf.score(x_test, y_test)  # 返回预测的准确度accuracy

# 画图
feature_name = ['效率', '介数', '办公', '中小学', '大学', '商业', '休闲', '医疗', '居住', '交通枢纽', '待开发面积', '距离', '混合用地熵']
dot_data = tree.export_graphviz(clf,
                                out_file='tree.dot',
                                feature_names=feature_name,
                                class_names=["1", "2", "3", '4', '5'],
                                filled=True,  # 填充颜色
                                rounded=True  # 画出的方块无棱角
                                )

with open("tree.dot", encoding='utf-8') as f:
    dot_graph = f.read()
graph = graphviz.Source(dot_graph.replace("helvetica", "FangSong"))
graph.view()
