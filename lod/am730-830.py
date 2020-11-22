import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import time
import os

# %matplotlib inline


# 修改字体 解决中文乱码
font = {'family': 'SimHei'}
matplotlib.rc('font', **font)

entry_names = {221: '北客站', 223: '北苑', 225: '运动公园', 227: '行政中心', 229: '凤城五路',
               231: '市图书馆', 233: '大明宫西', 235: '龙首原', 237: '安远门', 239: '北大街',
               241: '钟楼', 243: '永宁门', 245: '南稍门', 247: '体育场', 249: '小寨',
               251: '纬一街', 253: '会展中心', 255: '三爻', 257: '凤栖原', 259: '航天城', 261: '韦曲南'}

# 上午07:30-08:30出站
df = pd.read_csv('D:\\数据处理\\20171123.csv')

need_data = df[(df['EXIT_STATION_ID'] != 0) & (df['LINE_ID'] == 2) &
               (df['TRADE_TIME'] >= 20171123073000) & (df['TRADE_TIME'] < 20171123083100) &
               (df['DEVICE_ID'].astype(str).str.slice(0, 3) == '1F0')]
# 取进站ID和时间字段
column_data = pd.DataFrame({'EXIT_STATION_ID': need_data['EXIT_STATION_ID'], 'TRADE_TIME': need_data['TRADE_TIME']})

# 小时
# column_data['TRADE_TIME'] = pd.to_datetime(column_data['TRADE_TIME'].astype(str).str.slice(0, 10), format='%Y%m%d%H')
# 分钟
# column_data['TRADE_TIME'] = pd.to_datetime(needcolumn_data_data['TRADE_TIME'].astype(str).str.slice(0, 12), format='%Y%m%d%H%M')

# 5分钟
column_data['TRADE_TIME'] = pd.to_numeric(column_data['TRADE_TIME'].astype(str).str.slice(8, 12)).div(5)
column_data['TRADE_TIME'] = column_data['TRADE_TIME'].astype(str).str.slice(0, 3)

# 分组计数
group_data = column_data.groupby(['EXIT_STATION_ID', 'TRADE_TIME'])['TRADE_TIME'].size().reset_index(
    name='size').set_index('TRADE_TIME')
print(group_data.head(20))
group_data.to_excel('D:/数据处理/am0730-0830.xls')

nowTime = time.strftime("%Y%m%d%H%M%S", time.localtime())

# # 出图
# save_path = 'D:/数据处理/早上出站出图%s/' % nowTime
# # 创建图片保存文件夹
# os.makedirs(save_path)
# for i in entry_names.keys():
#     next_data = pd.DataFrame(group_data[group_data['EXIT_STATION_ID'] == i]['size'])
#     if next_data.size > 0:
#         img = next_data.plot(style='ob', alpha=0.3, figsize=(10, 5))
#         img.set_title(entry_names[i])
#         plt.savefig('%s%s.png' % (save_path, entry_names[i]))
#         plt.show()
