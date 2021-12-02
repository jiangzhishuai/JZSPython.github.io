import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

x = np.arange(0, 10*np.pi, 0.01)
y = np.sin(x)

plt.plot(x, y)
plt.show()

s = np.random.random(3142)*0.2

yy = s+y

plt.plot(x[0:628], yy[0:628])
plt.show()

b, a = signal.butter(8, 0.01, 'lowpass')   # 8为滤波器阶数，0.01为滤波器截止频率，lowpass为低通
filldata = signal.filtfilt(b, a, yy)

plt.plot(x[0:628], filldata[0:628])
plt.show()
