import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import seaborn
import os
import time
from matplotlib.font_manager import FontProperties
from sklearn.cluster import KMeans

# %matplotlib inline

# 修改字体 解决中文乱码
font = {
    'family' : 'SimHei'
}
matplotlib.rc('font', **font)

font_set = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=12)
entry_names = {221: '北客站', 223: '北苑', 225: '运动公园', 227: '行政中心', 229: '凤城五路',
               231: '市图书馆', 233: '大明宫西', 235: '龙首原', 237: '安远门', 239: '北大街',
               241: '钟楼', 243: '永宁门', 245: '南稍门', 247: '体育场', 249: '小寨',
               251: '纬一街', 253: '会展中心', 255: '三爻', 257: '凤栖原', 259: '航天城', 261: '韦曲南'}


Gate = pd.read_csv('D:\\数据处理\\20171123.csv')
Entrys, Exits, Time = Gate['ENTRY_STATION_ID'], Gate['EXIT_STATION_ID'], Gate['TRADE_TIME']
data = pd.DataFrame({'Time': Time, 'Entrys': Entrys, 'Exits': Exits})
data_time_str = data['Time'].astype(str).str.slice(0, 12)
data['Time'] = pd.to_datetime(data_time_str, format='%Y%m%d%H%M')
Endata = data[(data.Entrys != 0) & (data.Exits == 0)]
sort_Endata = Endata.sort_values(by=['Entrys', 'Time'])
group_data = sort_Endata.groupby(['Entrys', 'Time'])['Time'].size().reset_index(name='Size').set_index('Time')

nowTime = time.strftime("%Y%m%d%H%M%S", time.localtime())
save_path = 'D:/数据处理/出图%s/' % nowTime
# 创建图片保存文件夹
os.makedirs(save_path)

for i in entry_names.keys():
    # 分割并新建每个站台的DataFrame数据 进行画图
    next_data = pd.DataFrame(group_data[group_data.Entrys == i]['Size'])
    if next_data.size > 0:
        print(i)
        img = next_data.plot(style='ob', alpha=0.3, figsize=(10, 5))
        img.set_title(entry_names[i])
        plt.savefig('%s%s.png' % (save_path, str(i)))
        plt.show()

