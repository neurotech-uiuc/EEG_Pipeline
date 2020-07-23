import numpy as np
import matplotlib.pyplot as plt
import os
from scipy.fft import fft
from string import digits

dataLocation = "Recordings/SoftwareProject/"

# file names for the different recordings
rawDataLocs = os.listdir(dataLocation)

def getTitle(recordingFile):
  return recordingFile.split("-")[-1].split(".")[0].translate({ord(k): None for k in digits})

# pass none if dont want granularity
# pass none to dataLimit if want all the data
def getData(dataLoc, granularity, channel, dataLimit):
  
  dataFolder = "./Recordings/SoftwareProject/" + dataLoc + "/"
  dataFile = dataFolder + os.listdir(dataFolder)[0]

  dataRaw = []
  dataStartLine = 6
  count = 0
  for line in open(dataFile, 'r').readlines(): 
      if count >= dataStartLine:
          dataRaw.append(line.strip().split(','))
      else:
          count += 1
  dataRaw = np.char.strip(np.array(dataRaw))

  dataChannels = dataRaw[:, 1:5]

  if granularity is None:
    granularity = 1
  # the current channel of data
  if dataLimit is None:
    dataLimit = len(dataChannels)

  channelData = dataChannels[:,channel][:dataLimit:granularity]
  y = channelData.astype(float)
  x = np.arange(len(channelData))
  return x,y

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

def plotFFT(dataLoc, channel):
  # PARAMS: dataLoc, granilarity, channel, howmuchdatatouse
  x,y = getData(dataLoc, None, channel, None )
  xf, yf, N = fftData(x, y, None)

  title = getTitle(dataLoc)
  yf=2.0/N * np.abs(yf[0:N//2])

  a=len(yf)//100
  yf[int(a*59) : int(a*62)]= 0
  for i in range(0, len(yf) - a, a):
    average = sum(yf[i : i + a]) / a
    yf[i: i + a] = average

  plt.plot(xf, yf)

  plt.xlim(0, 100)
  # plt.ylim(0, 1000)

  plt.yscale('log')

  plt.grid()
  plt.xlabel("Channel " + str(channel))
  plt.title(title)
  plt.savefig("./Plots/FFT/fft_" + title + "_chan_" + str(channel) + '.png')
  plt.clf()

# plotFFT(rawDataLocs[0], 0)
for dataLoc in rawDataLocs:
  plotFFT(dataLoc, 0)