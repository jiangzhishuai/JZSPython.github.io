# '''读取数据'''
import numpy
import numpy as np
import matplotlib.pyplot as plt  # 导入绘图工作的函数集合
from openpyxl import load_workbook
import pandas as pd
import operator


# 获取Excel数据
wb = load_workbook('C:/Users/zhangming/Desktop/1114下午/平均值/000.xlsx')
sheets = wb.worksheets  # 获取当前所有的sheet

# 获取第一张sheet
sheet1 = sheets[0]
print(sheet1)

col1 = []
col2 = []
col3 = []
col4 = []
col5 = []
col6 = []
col7 = []
col8 = []
col9 = []
col10 = []
col11 = []
col12 = []
col13 = []
col14 = []
col15 = []
col16 = []
col17 = []
col18 = []

# 获取第一列所有数据
for col in sheet1['A'][1:100000]:
    col1.append(col.value)
for col in sheet1['B'][0:100000]:
    col2.append(col.value)
for col in sheet1['C'][1:100000]:
    col3.append(col.value)
for col in sheet1['D'][0:100000]:
    col4.append(col.value)

for col in sheet1['E'][1:100000]:
    col5.append(col.value)
for col in sheet1['F'][0:100000]:
    col6.append(col.value)
for col in sheet1['G'][1:100000]:
    col7.append(col.value)
for col in sheet1['H'][0:100000]:
    col8.append(col.value)

for col in sheet1['I'][1:100000]:
    col9.append(col.value)
for col in sheet1['J'][0:100000]:
    col10.append(col.value)
for col in sheet1['K'][1:100000]:
    col11.append(col.value)
for col in sheet1['L'][0:100000]:
    col12.append(col.value)

for col in sheet1['M'][1:100000]:
    col13.append(col.value)
for col in sheet1['N'][0:100000]:
    col14.append(col.value)
for col in sheet1['N'][1:100000]:
    col15.append(col.value)
for col in sheet1['P'][0:100000]:
    col16.append(col.value)


sum = 0
for j in range(100000):  # 循环逐行打印
   m = cola[j]  # 获取第i列的数字
   n = abs(m)   # 绝对值
   sum += n
Umean = sum / 100000  # 计算平均能量

col17.append(sum)
col18.append(Umean)

# print(col2)
print(col17)
print(col18)

