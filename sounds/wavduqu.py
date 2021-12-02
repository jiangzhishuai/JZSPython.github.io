from scipy.io import wavfile
import numpy as np
import pandas as pd

sample_rate, sig = wavfile.read('C:/Users/zhangming/Desktop/互联网大赛/48.wav')
print("采样率: %d" % sample_rate)
print(sig)

if sig.dtype == np.int16:
    print("PCM16位整形")
if sig.dtype == np.float32:
    print("PCM32位浮点")

array_1 = sig
data = pd.DataFrame(sig)

writer = pd.ExcelWriter('C:/Users/zhangming/Desktop/互联网大赛/test2.xlsx')
data.to_excel(writer, 'sheet_1', float_format='%.2f')
writer.save()
writer.close()
print("END")