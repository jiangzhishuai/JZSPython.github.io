import numpy as np
import wave
import matplotlib.pyplot as plt
wlen=512
inc=128
f = wave.open(r"D:/Jiangshuai/研一/0000/研一下/ICA声音分离/ICA会议论文/声音/压缩机.wav", "rb")
params = f.getparams()
nchannels, sampwidth, framerate, nframes = params[:4]
str_data = f.readframes(nframes)
wave_data = np.fromstring(str_data, dtype=np.short)
wave_data = wave_data*1.0/(max(abs(wave_data)))
print(wave_data[:10])
signal_length=len(wave_data) # 信号总长度
if signal_length<=wlen: # 若信号长度小于一个帧的长度，则帧数定义为1
        nf=1
else: # 否则，计算帧的总长度
        nf=int(np.ceil((1.0*signal_length-wlen+inc)/inc))
print(nf)
pad_length=int((nf-1)*inc+wlen) #所有帧加起来总的铺平后的长度
zeros=np.zeros((pad_length-signal_length,)) #不够的长度使用0填补，类似于FFT中的扩充数组操作
pad_signal=np.concatenate((wave_data,zeros)) #填补后的信号记为pad_signal
indices=np.tile(np.arange(0,wlen),(nf,1))+np.tile(np.arange(0,nf*inc,inc),(wlen,1)).T  #相当于对所有帧的时间点进行抽取，得到nf*nw长度的矩阵
print(indices[:2])
indices=np.array(indices,dtype=np.int32) #将indices转化为矩阵
frames=pad_signal[indices] #得到帧信号
windown=np.hanning(wlen)
d=np.zeros(nf)
x=np.zeros(nf)
time = np.arange(0,nf) * (inc*1.0/framerate)
for i in range(0,nf):
        a=frames[i:i+1]
        b = a[0] * windown
        c=np.square(b)
        d[i]=np.sum(c)
d = d*1.0/(max(abs(d)))
print(d)
plt.figure(figsize=(10,4))
plt.plot(time,d,c="g")
plt.grid()
plt.show()
