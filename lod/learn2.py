import pandas as pd
import matplotlib.pyplot as plt
import time
import os

df = pd.read_csv('D:\\数据处理\\20171123.csv')
df1 = df[(df['ENTRY_STATION_ID'] != 0) & (df['EXIT_STATION_ID'] == 0)]
# 小时
# df1['TRADE_TIME'] = pd.to_datetime(df1['TRADE_TIME'].astype(str).str.slice(0, 10), format='%Y%m%d%H')
# 分钟
df1['TRADE_TIME'] = pd.to_datetime(df1['TRADE_TIME'].astype(str).str.slice(0, 12), format='%Y%m%d%H%M')
df2 = pd.DataFrame({'ticket': df1['TICKET_TYPE'], 'time': df1['TRADE_TIME']})
group_data = df2.groupby(['ticket', 'time'])['time'].size().reset_index(name='size').set_index('time')

nowTime = time.strftime("%Y%m%d%H%M%S", time.localtime())
save_path = 'D:/数据处理/出图%s/' % nowTime
# 创建图片保存文件夹
os.makedirs(save_path)

for i in [256, 257, 258, 259, 261, 8448, 12544, 12545, 16384, 39168]:
    next_data = pd.DataFrame(group_data[group_data['ticket'] == i]['size'])
    if next_data.size > 0:
        img = next_data.plot(style='ob', alpha=0.3, figsize=(10, 5))
        img.set_title(str(i))
        plt.savefig('%s%s.png' % (save_path, str(i)))
        plt.show()
