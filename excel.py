import urllib
import urllib.request
import io
import sys
import xlsxwriter
import time
import logging
from xlrd import open_workbook
from xlutils.copy import copy
import socket
import os

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

ss = {'后卫寨','三桥','皂河','枣园','汉城路','开远门','劳动路','玉祥门','洒金桥','五路口','朝阳门','康复路','通化门','万寿路','长乐坡','浐河','半坡','纺织城','北客站','北苑','运动公园','行政中心','凤城五路','市图书馆','大明宫西','龙首原','安远门','北大街','钟楼','永宁门','南稍门','体育场','小寨','纬一街','会展中心','三爻','凤栖原','航天城','韦曲南','鱼化寨','丈八北路','延平门','科技路','太白南路','吉祥村','大雁塔','北池头','青龙寺','延兴门','咸宁路','长乐公园','胡家庙','石家街','辛家庙','广泰门','桃花潭','浐灞中心','香湖湾','务庄','国际港务区','双寨','新筑','保税区'}

rb = open_workbook('D:/数据处理/abc.xls')
wb = copy(rb)
ws = wb.get_sheet(0)
count = 0
for i in entry_names.keys():
    ws.write(0, count, entry_names[i])
    count = count + 1
wb.save('D:/数据处理/abc.xls')