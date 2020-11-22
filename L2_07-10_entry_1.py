import pandas as pd
import matplotlib
import numpy as np
import matplotlib.pyplot as plt

# %matplotlib inline


# ------曲线拟合------
# 修改字体 解决中文乱码
from scipy.optimize import curve_fit

font = {'family': 'SimHei'}
matplotlib.rc('font', **font)

entry_names = {221: '北客站', 223: '北苑', 225: '运动公园', 227: '行政中心', 229: '凤城五路',
               231: '市图书馆', 233: '大明宫西', 235: '龙首原', 237: '安远门', 239: '北大街',
               241: '钟楼', 243: '永宁门', 245: '南稍门', 247: '体育场', 249: '小寨',
               251: '纬一街', 253: '会展中心', 255: '三爻', 257: '凤栖原', 259: '航天城', 261: '韦曲南'}

entry_names2 = {227: '行政中心'}

df = pd.read_csv('D:\\数据处理\\20171123_L2.csv')

# 上午07:00-10:00进站
need_data = df[(df['ENTRY_STATION_ID'] != 0) & (df['LINE_ID'] == 2) &
               (df['TRADE_TIME'] >= 20171123070000) & (df['TRADE_TIME'] < 20171123100100)]

# 取进站ID和时间字段
column_data = pd.DataFrame({'station': need_data['ENTRY_STATION_ID'], 'time': need_data['TRADE_TIME']})

# 分钟转为小数 + 小时 保证连续
column_data['time'] = pd.to_numeric(column_data['time'].astype(str).str.slice(10, 12)).div(60).add(pd.to_numeric(column_data['time'].astype(str).str.slice(8, 10)))


# nowTime = time.strftime("%Y%m%d%H%M%S", time.localtime())
# save_path = 'D:/数据处理/出图%s/' % nowTime
# # 创建图片保存文件夹
# os.makedirs(save_path)

def func(x, a, u, sig):
    return a * (np.exp(-(x - u) ** 2 / (2 * sig ** 2)) / (np.math.sqrt(2 * np.math.pi) * sig)) * (431 + (4750 / x))


for i in entry_names.keys():
    # 筛选各站数据
    loc_data = column_data.loc[column_data["station"] == i]
    # 分组计数
    group_data = loc_data.groupby(['time'])['time'].size().reset_index(name='size').set_index('time')

    # if group_data.size > 0:
    #     img = group_data.plot(style='ob', alpha=0.3, figsize=(10, 5))
    #     img.set_title(entry_names[i])
    #     # plt.savefig('%s%s.png' % (save_path, entry_names[i]))
    #     plt.show()

    # 函数拟合
    # 拟合高斯分布的方法。
    # 自定义函数 func e指数形式

    # 定义x、y散点坐标
    x = group_data.index.values
    x = np.array(x)
    num = group_data['size'].values
    y = np.array(num)

    popt, pcov = curve_fit(func, x, y, p0=[3.1, 4.2, 3.3])
    # 获取popt里面是拟合系数
    a = popt[0]
    u = popt[1]
    sig = popt[2]

    yvals = func(x, a, u, sig)  # 拟合y值
    print(entry_names[i] + u'系数a:', a)
    print(entry_names[i] + u'系数u:', u)
    print(entry_names[i] + u'系数sig:', sig)
    print()

    # 绘图
    plot1 = plt.plot(x, y, 's', label='实际值')
    plot2 = plt.plot(x, yvals, 'r', label='拟合值')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend(loc=4)  # 指定legend的位置右下角
    plt.title(entry_names[i] + '函数拟合')
    plt.show()



