import numpy as np
from scipy.fftpack import fft,ifft
from openpyxl import load_workbook
from scipy.fftpack import fft
import matplotlib.pyplot as plt
from matplotlib.pylab import mpl

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
C = col2[700000:800000]

# -------------------  傅里叶变换 -------------------------
def fu( A,B ):
    mpl.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文
    mpl.rcParams['axes.unicode_minus'] = False  # 显示负号

    N = 100000
    x = A
    y = B

    fft_y = fft(y)  # 快速傅里叶变换

    x = np.arange(N)  # 频率个数
    half_x = x[range(int(N / 2))]   # 取一半区间

    angle_y = np.angle(fft_y)       # 取复数的角度

    abs_y = np.abs(fft_y)               # 取复数的绝对值，即复数的模(双边频谱)
    normalization_y = abs_y / (N / 2)   # 归一化处理（双边频谱）
    normalization_y[0] /= 2             # 归一化处理（双边频谱）
    normalization_half_y = normalization_y[range(int(N / 2))]  # 由于对称性，只取一半区间（单边频谱）


    # plt.subplot(211)
    # plt.plot(x, y)
    # plt.ylim(-10, 10)
    # plt.title('时域图')
    # plt.subplot(212)
    plt.xlim(0, 50000)
    plt.plot(half_x, normalization_half_y, 'blue')
    plt.title('单边振幅谱(归一化)', fontsize=9, color='blue')

    plt.show()
fu(A,C)
