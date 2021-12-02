import numpy as np
from scipy.fftpack import fft, ifft
import matplotlib.pyplot as plt
from matplotlib.pylab import mpl


a = 0.08
b = 0.23
x1 = (Et/E0)**b
x2 = ((0.5+0.5*(E/Et))**b-1)
x3 = (sone/Bark)