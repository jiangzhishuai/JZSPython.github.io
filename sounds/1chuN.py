from scipy import signal
import numpy as np
import matplotlib.pyplot as plt
import math

sampleRate = 44100.0
nyquistRate = sampleRate/2.0

#center = [39, 50, 63, 79, 99, 125, 157, 198, 250, 315, 397, 500, 630, 
# 794, 1000, 1260, 1588, 2000, 2520, 3176, 4000, 5040, 6352, 8000, 10080,
# 12704, 16000, 20160, 2508, 32000]
centerFrequency_Hz = 480.0
lowerCutoffFrequency_Hz = centerFrequency_Hz/math.sqrt(2)
upperCutoffFrequenc_Hz = centerFrequency_Hz*math.sqrt(2)

# Determine numerator (b) and denominator (a) coefficients of the digital 
# Infinite Impulse Response (IIR) filter.
b, a = signal.butter( N=4, Wn=np.array([ lowerCutoffFrequency_Hz, 
upperCutoffFrequenc_Hz])/nyquistRate, btype='bandpass', analog=False, 
output='ba')

# Compute frequency response of the filter.
w, h = signal.freqz(b, a)

fig = plt.figure()
plt.title('Digital filter frequency response')
ax1 = fig.add_subplot(111)

plt.plot(w, 20 * np.log10(abs(h)), 'b')
plt.ylabel('Amplitude [dB]', color='b')
plt.xlabel('Frequency [rad/sample]')

ax2 = ax1.twinx()
angles = np.unwrap(np.angle(h))
plt.plot(w, angles, 'g')
plt.ylabel('Angle (radians)', color='g')
plt.grid()
plt.axis('tight')
plt.show()

fs, speech = wavfile.read(filename='segmented/atb30.wav');
speech = speech[:, 0]
fig=plt.figure()
plt.title('Speech Signal')
plt.plot(speech)

filteredSpeech=signal.filtfilt(b, a, speech)
fig=plt.figure()
plt.title('480 Hz Octave-band Filtered Speech')
plt.plot(filteredSpeech)