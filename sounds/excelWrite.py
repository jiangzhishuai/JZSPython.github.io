import matplotlib.pyplot as plt
import numpy as np
from openpyxl import load_workbook

# 获取Excel数据
wb = load_workbook('C:/Users/zhangming/Desktop/采集卡1210/1003数据/方波/示波器数据.xlsx')
sheets = wb.worksheets  # 获取当前所有的sheet

# 获取第一张sheet
sheet1 = sheets[0]
print(sheet1)

# 获取第一列所有数据
col1 = []
for col in sheet1['A']:
    col1.append(col.value)

A = col1
print(len(A))
# AA = B[:20000]

sum = 0
for i in range(0 , len(A)):
    sum += abs(A[i])
print(sum / 300)
