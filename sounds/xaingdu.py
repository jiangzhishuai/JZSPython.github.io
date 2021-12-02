from soundBase import soundBase

# 2.3 练习1
sb = soundBase('D:/Jiangshuai/研一/0000/研一下/声音分离/风扇.wav')
data, fs, nbits = sb.audioread()
# sb.SPL(data, fs)
spl, freq = sb.iso226(50)
