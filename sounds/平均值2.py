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

# 获取第一列所有数据
for col in sheet1['A'][1:100000]:
    col1.append(col.value)

sum = 0
for j in range(len(col1)):  # 循环逐行打印
   m = col1[j]  # 获取第i列的数字
   n = abs(m)   # 绝对值
   sum += n
Umean = sum / len(col1)  # 计算平均能量

col2.append(sum)
col3.append(Umean)

# print(col2)
print(col2)
print(col3)

