import numpy as np
from openpyxl import load_workbook
import matplotlib.pyplot as plt
from scipy.io import wavfile
from numpy import log10


# --------------获取Excel数据-----------------
wb = load_workbook('C:/Users/zhangming/Desktop/采集卡1210/1021数据/组件.xlsx')
sheets = wb.worksheets  # 获取当前所有的sheet
print(sheets)

# 获取第一张sheet
sheet1 = sheets[0]
print(sheet1)

# 获取第一列所有数据  存到数组col1中  时间
col1 = []
for col in sheet1['A'][22001:24000]:
    col1.append(col.value)

# 获取第二列所有数据  存到数组col2中  电压
col2 = []
for col in sheet1['B'][22001:24000]:
    col2.append(col.value)
B = col2

# --------------傅里叶变换----------------

def stftAnal(x, w, N, H):
    """
    x: 输入信号, w: 分析窗, N: FFT 的大小, H: hop 的大小
    返回 xmX, xpX: 振幅和相位，以 dB 为单位
    """

    M = w.size                                      # 分析窗的大小
    hM1 = (M+1)//2
    hM2 = M//2
    x = np.append(np.zeros(hM2),x)                  # 在信号 x 的最前面与最后面补零
    x = np.append(x,np.zeros(hM2))
    pin = hM1                                       # 初始化指针，用来指示现在指示现在正在处理哪一帧
    pend = x.size-hM1                               # 最后一帧的位置
    w = w / sum(w)                                  # 归一化分析窗
    xmX = []
    xpX = []
    while pin<=pend:
        x1 = x[pin-hM1:pin+hM2]                     # 选择一帧输入的信号
        mX, pX = dftAnal(x1, w, N)              # 计算 DFT（这个函数不是库中的）
        xmX.append(np.array(mX))                    # 添加到 list 中
        xpX.append(np.array(pX))
        pin += H                                    # 更新指针指示的位置
    xmX = np.array(xmX)                             # 转换为 numpy 数组
    xpX = np.array(xpX)
    return xmX, xpX


def TFCT(trame, Fe, Nfft, fenetre, Nwin, Nhop):
    L = round((len(trame) - len(fenetre)) / Nhop) + 1
    M = Nfft
    xmat = np.zeros((M, L))
    print('xmat', xmat.shape)
    print(Nwin + Nhop)
    for j in range(L):
        xmat[:, j] = np.fft.fft(trame[j * Nhop:Nwin + Nhop * j] * fenetre, Nfft)
    x_temporel = np.linspace(0, (1 / Fe) * len(trame), len(trame))
    x_frequentiel = np.linspace(0, Fe, Nfft)

    return xmat, x_temporel, x_frequentiel

TFCT(B, 200000, 256, hann, 256, 128)
