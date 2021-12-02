'''分帧'''
import numpy as np
import librosa.display  # 导入音频及绘图显示包
import matplotlib.pyplot as plt  # 导入绘图工作的函数集合

# 读取音频文件
# 读取语音文件并绘制波形图
times = librosa.get_duration(filename='D:\任务\Bluesky1.wav')  # 获取音频时长
# 返回音频采样数组及采样率
y, sr = librosa.load('D:\任务\Bluesky1.wav', sr=8000, offset=0.0, duration=None)
x = np.arange(0, times, 1/sr)  # 时间刻度
# 绘制图形
plt.plot(x, y)
plt.xlabel('times')  # x轴时间
plt.ylabel('amplitude')  # y轴振幅
plt.title('bluesky1.wav', fontsize=12, color='black')  # 标题名称、字体大小、颜色
plt.show()

# 分帧
def frame(x, lframe, mframe):  # 定义分帧函数
    signal_length = len(x)  # 获取语音信号的长度
    fn = (signal_length-lframe)/mframe  # 分成fn帧
    fn1 = np.ceil(fn)  # 将帧数向上取整，如果是浮点型则加一
    fn1 = int(fn1)  # 将帧数化为整数
    # 求出添加的0的个数
    numfillzero = (fn1*mframe+lframe)-signal_length
    # 生成填充序列
    fillzeros = np.zeros(numfillzero)
    # 填充以后的信号记作fillsignal
    fillsignal = np.concatenate((x,fillzeros))  # concatenate连接两个维度相同的矩阵
    # 对所有帧的时间点进行抽取，得到fn1*lframe长度的矩阵d
    d = np.tile(np.arange(0, lframe), (fn1, 1)) + np.tile(np.arange(0, fn1*mframe, mframe), (lframe, 1)).T
    # 将d转换为矩阵形式（数据类型为int类型）
    d = np.array(d, dtype=np.int32)
    signal = fillsignal[d]
    return(signal, fn1, numfillzero)
lframe = int(sr*0.025)  # 帧长(持续0.025秒)
mframe = int(sr*0.001)  # 帧移
# 函数调用，把采样数组、帧长、帧移等参数传递进函数frame，并返回存储于endframe、fn1、numfillzero中
endframe, fn1, numfillzero = frame(y, lframe, mframe)

# 显示第1帧波形图
x1 = np.arange(0, lframe, 1)  # 第1帧采样点刻度
x2 = np.arange(0, lframe/sr, 1/sr)  # 第1帧时间刻度
# 显示波形图
plt.figure()
plt.plot(x1, endframe[0])
plt.xlabel('points')  # x轴
plt.ylabel('wave')  # y轴
plt.title('bluesky1 firstframe  wave', fontsize=12, color='black')
plt.show()
plt.figure()
plt.plot(x2, endframe[0])
plt.xlabel('time')  # x轴
plt.ylabel('wave')  # y轴
plt.title('bluesky1 firstframe  wave', fontsize=12, color='black')
plt.show()
