import pandas as pd
import numpy
import numpy as np
import matplotlib.pyplot as plt  # 导入绘图工作的函数集合
from openpyxl import load_workbook
import operator

# -------------------  读取txt数据 存储到数组data里-------------------------

# with open("C:/Users/zhangming/Desktop/1119下午/无多余物/1.txt", "r") as f:  # 打开文件
with open("C:/Users/zhangming/Desktop/1119下午/11.19/焊锡/(1).txt", "r") as f:  # 打开文件
   # data = f.read().splitlines()   # 去除换行符号
   data = f.readlines()             # 直接出去  不去除\n
   f.close()

B = np.array(data)  #  list 转 narry

col2 = []
# 遍历数组 转化为float
for i in B[2:len(B)]:
    col2.append(float(i))
print(len(col2))

# print(D)


# -------------------  读取#EXCE 数据 存储到数组time横坐标里-------------------------
wb = load_workbook('C:/Users/zhangming/Desktop/1119下午/time.xlsx')
sheets = wb.worksheets  # 获取当前所有的sheet

# 获取第一张sheet
sheet1 = sheets[0]
print(sheet1)

# 获取第一列所有数据
col1 = []
for col in sheet1['A'][0:100000]:
    col1.append(col.value)
A = np.array(col1)
C = col2[0:100000]

print(type(A))
print(type(B))


# 绘图函数
def huitu( A,B ):  # (时间，电压)
   # 读取音频文件
   y = B
   x = A  # 时间刻度
   # 绘制图形
   plt.plot(x, y)
   plt.xlabel('t/s')  # x轴时间
   plt.ylabel('U/V')  # y轴振幅
   plt.title('shiyutu', fontsize=12, color='black')  # 标题名称、字体大小、颜色
   plt.ylim(-10, 10)
   plt.show()


# 使得几秒的数据分段显示
a = len(col2) // 100000
print(a)

for b in range(0, a, 1):  # 循环逐行
    D = col2[b * 100000: b * 100000 + 100000]
    huitu(A, C)
