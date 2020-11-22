import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import time
import os

# %matplotlib inline


# 修改字体 解决中文乱码
font = {'family': 'SimHei'}
matplotlib.rc('font', **font)

entry_names = {
    121: '后卫寨', 123: '三桥', 125: '皂河', 127: '枣园', 129: '汉城路',
    131: '开远门', 133: '劳动路', 135: '玉祥门', 137: '洒金桥', 139: '北大街',
    141: '五路口', 143: '朝阳门', 145: '康复路', 147: '通化门', 149: '万寿路',
    151: '长乐坡', 153: '浐河', 155: '半坡', 157: '纺织城',
    221: '北客站', 223: '北苑', 225: '运动公园', 227: '行政中心', 229: '凤城五路',
    231: '市图书馆', 233: '大明宫西', 235: '龙首原', 237: '安远门', 239: '北大街',
    241: '钟楼', 243: '永宁门', 245: '南稍门', 247: '体育场', 249: '小寨',
    251: '纬一街', 253: '会展中心', 255: '三爻', 257: '凤栖原', 259: '航天城', 261: '韦曲南',
    321: '鱼化寨', 323: '丈八北路', 325: '延平门', 327: '科技路', 329: '太白南路',
    331: '吉祥村', 333: '小寨', 335: '大雁塔', 337: '北池头', 339: '青龙寺',
    341: '延兴门', 343: '咸宁路', 345: '长乐公园', 347: '通化门', 349: '胡家庙',
    351: '石家街', 353: '辛家庙', 355: '广泰门', 357: '桃花潭', 359: '浐灞中心',
    361: '香湖湾', 363: '务庄', 365: '国际港务区', 367: '双寨', 369: '新筑', 371: '保税区'}

# 上午07:30-08:30 早上7.30-8.30的进出站之和 要把闸机筛了
df = pd.read_csv('D:\\数据处理\\YKT20171123 2点-18点.csv')

# 出站
out_need_data = df[(df['EXIT_STATION_ID'] != 0) &
               (df['TRADE_TIME'] >= 20171123070000) & (df['TRADE_TIME'] < 20171123100100) &
               (df['DEVICE_ID'].astype(str).str.slice(0, 3) == '1F0')]
# 取出站ID和时间字段
out_column_data = pd.DataFrame({'OUT_STATION_ID': out_need_data['EXIT_STATION_ID'], 'TRADE_TIME': out_need_data['TRADE_TIME']})
# 5分钟
out_column_data['TRADE_TIME'] = pd.to_numeric(out_column_data['TRADE_TIME'].astype(str).str.slice(8, 12)).div(5)
out_column_data['TRADE_TIME'] = pd.to_numeric(out_column_data['TRADE_TIME'].astype(str).str.slice(0, 3)).mul(5)
# 分组计数
out_group_data = out_column_data.groupby(['OUT_STATION_ID', 'TRADE_TIME'])['TRADE_TIME'].size().reset_index(
    name='OUT_SIZE').set_index('TRADE_TIME')

out_column_data['TRADE_TIME'] = pd.to_numeric(out_column_data['TRADE_TIME']).div(5)

out_group_data.to_excel('D:/数据处理/all_am_out_0700-1000.xls')
print(out_group_data.head(10))