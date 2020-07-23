import numpy as np
import matplotlib.pyplot as plt
import os
from scipy.fft import fft
from string import digits

dataLocation = "Recordings/SoftwareProject/"

# file names for the different recordings
rawDataLocs = os.listdir(dataLocation)

def getFileLocs(dataLoc):
  return(os.listdir(dataLoc))


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

