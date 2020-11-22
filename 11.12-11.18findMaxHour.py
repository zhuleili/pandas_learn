import pandas as pd
import matplotlib
import numpy as np
import matplotlib.pyplot as plt

station = ['后卫寨', '三桥', '皂河', '枣园', '汉城路', '开远门', '劳动路', '玉祥门', '洒金桥', '北大街1', '五路口合', '朝阳门', '康复路', '通化门1', '万寿路',
           '长乐坡', '浐河', '半坡', '纺织城', '北客站', '北苑', '运动公园', '行政中心合', '凤城五路', '市图书馆', '大明宫西', '龙首原', '安远门', '北大街2', '钟楼',
           '永宁门', '南稍门', '体育场', '小寨合', '纬一街', '会展中心', '三爻', '凤栖原', '航天城', '韦曲南', '鱼化寨', '丈八北路', '延平门', '科技路', '太白南路',
           '吉祥村', '大雁塔合', '北池头', '青龙寺', '延兴门', '咸宁路', '长乐公园', '通化门3', '胡家庙', '石家街', '辛家庙', '广泰门', '桃花潭', '浐灞中心',
           '香湖湾', '务庄', '国际港务区', '双寨', '新筑', '保税区', '航天新城', '航天东路', '神舟大道', '东长安街', '飞天路', '航天大道', '金滹沱', '曲江池西',
           '大唐芙蓉园', '西安科技大学', '建筑科技大学·李家村', '和平门', '大差市', '火车站', '含元殿', '大明宫', '大明宫北', '余家寨', '百花村',
           '常青路', '市中医医院', '文景路', '凤城九路', '凤城十二路', '元朔路', '北客站(北广场)']
times = ['225', '226', '227', '228', '301', '302', '303']
for t in times:
    df = pd.read_excel("D:\\数据处理\\dealwith2\\线路分时段客运量统计报表20190%s.xlsx" % t, header=0, names=None)
    df.eval('小寨合 = 小寨2 + 小寨3', inplace=True)
    df.eval('大雁塔合 = 大雁塔3 + 大雁塔4', inplace=True)
    df.eval('五路口合 = 五路口1 + 五路口4', inplace=True)
    df.eval('行政中心合 = 行政中心2 + 行政中心4', inplace=True)
    result_data = pd.DataFrame({'in_out': ['am_in', 'am_out', 'pm_in', 'pm_out']})
    for i in station:
        print('正在计算20190%s' % t)
        result = []
        result_1h = []
        result_15m = []
        result_time = []
        col = pd.DataFrame({'id': df['id'], 'time': df['time'], 'inout': df['inout'], i: df[i]})
        am_in = col[(col['id'] <= 144) & (col['inout'] == '进站')]
        am_in['max'] = am_in[i].rolling(4).max()
        am_in['sum'] = am_in[i].rolling(4).sum()
        x = np.array(am_in.loc[am_in['sum'].idxmax(), ['max']])[0]  # 1小时里面15分钟的最大量
        y = am_in['sum'].max()  # 一小时最大量
        result_15m.append(x)
        result_1h.append(y)
        result.append(x * 4 / y)
        time1 = np.array(am_in.loc[am_in['sum'].idxmax() - 9, ['time']])[0]
        time2 = np.array(am_in.loc[am_in['sum'].idxmax(), ['time']])[0]
        result_time.append(time1[0:5] + '-' + time2[8:])

        am_out = col[(col['id'] <= 144) & (col['inout'] == '出站')]
        am_out['max'] = am_out[i].rolling(4).max()
        am_out['sum'] = am_out[i].rolling(4).sum()
        x = np.array(am_out.loc[am_out['sum'].idxmax(), ['max']])[0]  # 1小时里面15分钟的最大量
        y = am_out['sum'].max()  # 一小时最大量
        result_15m.append(x)
        result_1h.append(y)
        result.append(x * 4 / y)
        time1 = np.array(am_out.loc[am_out['sum'].idxmax() - 9, ['time']])[0]
        time2 = np.array(am_out.loc[am_out['sum'].idxmax(), ['time']])[0]
        result_time.append(time1[0:5] + '-' + time2[8:])

        pm_in = col[(col['id'] > 192) & (col['inout'] == '进站')]
        pm_in['max'] = pm_in[i].rolling(4).max()
        pm_in['sum'] = pm_in[i].rolling(4).sum()
        x = np.array(pm_in.loc[pm_in['sum'].idxmax(), ['max']])[0]  # 1小时里面15分钟的最大量
        y = pm_in['sum'].max()  # 一小时最大量
        result_15m.append(x)
        result_1h.append(y)
        result.append(x * 4 / y)
        time1 = np.array(pm_in.loc[pm_in['sum'].idxmax() - 9, ['time']])[0]
        time2 = np.array(pm_in.loc[pm_in['sum'].idxmax(), ['time']])[0]
        result_time.append(time1[0:5] + '-' + time2[8:])

        pm_out = col[(col['id'] > 192) & (col['inout'] == '出站')]
        pm_out['max'] = pm_out[i].rolling(4).max()
        pm_out['sum'] = pm_out[i].rolling(4).sum()
        x = np.array(pm_out.loc[pm_out['sum'].idxmax(), ['max']])[0]  # 1小时里面15分钟的最大量
        y = pm_out['sum'].max()  # 一小时最大量
        result_15m.append(x)
        result_1h.append(y)
        result.append(x * 4 / y)
        time1 = np.array(pm_out.loc[pm_out['sum'].idxmax() - 9, ['time']])[0]
        time2 = np.array(pm_out.loc[pm_out['sum'].idxmax(), ['time']])[0]
        result_time.append(time1[0:5] + '-' + time2[8:])

        result_data[i + 'time'] = result_time
        result_data[i + '15m'] = result_15m
        result_data[i + '1h'] = result_1h
        result_data[i] = result
    # print(result_data)

    result_data.to_excel('D:/数据处理/dealwith2/20200709出全数据20190%s线路小时高峰.xlsx' % t)
print('完成')




