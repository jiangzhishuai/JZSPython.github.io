'''读取数据'''
import numpy as np
import matplotlib.pyplot as plt  # 导入绘图工作的函数集合
from openpyxl import load_workbook


# 获取Excel数据
wb = load_workbook('C:/Users/zhangming/Desktop/采集卡1210/1021数据/多余物.xlsx')
sheets = wb.worksheets  # 获取当前所有的sheet

# 获取第一张sheet
sheet1 = sheets[0]
print(sheet1)

# 获取第一列所有数据
col1 = []
for col in sheet1['A'][0:200000]:
    col1.append(col.value)
col2 = []
for col in sheet1['B'][0:200000]:
    col2.append(col.value)

# 读取音频文件

y = col2
x = col1  # 时间刻度
# 绘制图形
plt.plot(x, y)
plt.xlabel('times')  # x轴时间
plt.ylabel('amplitude')  # y轴振幅
plt.title('bluesky1.wav', fontsize=12, color='black')  # 标题名称、字体大小、颜色
plt.ylim(-10, 10)
plt.show()

