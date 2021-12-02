import pandas as pd
import numpy
import numpy as np
from scipy.fftpack import fft,ifft
from scipy.fftpack import fft,ifft
import matplotlib.pyplot as plt
from matplotlib.pylab import mpl


# -------------------  读取txt数据 存储到数组data里-------------------------

# with open("C:/Users/zhangming/Desktop/1119下午/无多余物/1.txt", "r") as f:  # 打开文件
from pingjunnnegliang import nf

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
A = col1
C = col2[0:100000]


mpl.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文
mpl.rcParams['axes.unicode_minus'] = False  # 显示负号

# 采样点选择1400个，因为设置的信号频率分量最高为600赫兹，根据采样定理知采样频率要大于信号频率2倍，所以这里设置采样频率为1400赫兹（即一秒内有1400个采样点，一样意思的）
x = np.linspace(0, 1, 1400)
print()
print(x)

# 设置需要采样的信号，频率分量有200，400和600
y = 7 * np.sin(2 * np.pi * 200 * x) + 5 * np.sin(2 * np.pi * 400 * x) + 3 * np.sin(2 * np.pi * 600 * x)
print()
print(y)
fft_y = fft(y)  # 快速傅里叶变换
"""
N = 1400
x = np.arange(N)  # 频率个数
half_x = x[range(int(N / 2))]  # 取一半区间

abs_y = np.abs(fft_y)  # 取复数的绝对值，即复数的模(双边频谱)
angle_y = np.angle(fft_y)  # 取复数的角度
normalization_y = abs_y / N  # 归一化处理（双边频谱）
normalization_half_y = normalization_y[range(int(N / 2))]  # 由于对称性，只取一半区间（单边频谱）

plt.subplot(231)
plt.plot(x, y)
plt.title('原始波形')

plt.subplot(232)
plt.plot(x, fft_y, 'black')
plt.title('双边振幅谱(未求振幅绝对值)', fontsize=9, color='black')

plt.subplot(233)
plt.plot(x, abs_y, 'r')
plt.title('双边振幅谱(未归一化)', fontsize=9, color='red')

plt.subplot(234)
plt.plot(x, angle_y, 'violet')
plt.title('双边相位谱(未归一化)', fontsize=9, color='violet')

plt.subplot(235)
plt.plot(x, normalization_y, 'g')
plt.title('双边振幅谱(归一化)', fontsize=9, color='green')

plt.subplot(236)
plt.plot(half_x, normalization_half_y, 'blue')
plt.title('单边振幅谱(归一化)', fontsize=9, color='blue')

plt.show()

"""