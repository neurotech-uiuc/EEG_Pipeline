import numpy as np
import matplotlib.pyplot as plt
import os
from scipy.fft import fft
from string import digits

def fftData(x, y, N):
  # https://docs.scipy.org/doc/scipy/reference/tutorial/fft.html
  # N = frequency limiter
  if N == None:
    N = len(x)

  # sample spacing
  T = 0.005
  # x = np.arange(len(channel))
  # y = channel0.astype(float)
  yf = fft(y)
  xf = np.linspace(0.0, 1.0/(2.0*T), N//2)
  return xf, yf, N