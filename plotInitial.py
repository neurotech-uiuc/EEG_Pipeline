import numpy as np
import matplotlib.pyplot as plt
import os
from datetime import datetime
from string import digits

def plot_initial(plot_type, title):
    dataLocation = "./Recordings/SoftwareProject/"
    os.listdir(dataLocation)
    singleBlinkLoc = dataLocation + plot_type
    # print(os.listdir(singleBlinkLoc)[0])
    singleBlinkLoc = singleBlinkLoc + os.listdir(singleBlinkLoc)[0]
    dataStartLine = 6
    singleBlinkRaw = []
    count = 0
    for line in open(singleBlinkLoc, 'r').readlines(): 
        if count >= dataStartLine:
            singleBlinkRaw.append(line.strip().split(','))
        else:
            count += 1
    singleBlinkRaw = np.char.strip(np.array(singleBlinkRaw))
    
    granularity = 10
    # getting just the data channels recorded
    singleBlinkChannels = singleBlinkRaw[:, 1:5]
    singleBlinkTime = singleBlinkRaw[:, 8:9]

    timeThing = "15:30:25.402"
    datetime_object = datetime.strptime(timeThing, '%H:%M:%S.%f')
    data = singleBlinkChannels[:,0][::granularity]

    channel0 = singleBlinkChannels[:,0][:500:granularity]
    channel1 = singleBlinkChannels[:,1][:500:granularity]
    channel2 = singleBlinkChannels[:,2][:500:granularity]
    channel3 = singleBlinkChannels[:,3][:500:granularity]    

    plt.plot(np.arange(len(channel0)), channel0.astype(float), label = 'Channel 0')
    plt.plot(np.arange(len(channel1)), channel1.astype(float), label = 'Channel 1')
    plt.plot(np.arange(len(channel2)), channel2.astype(float), label = 'Channel 2')
    plt.plot(np.arange(len(channel3)), channel3.astype(float), label = 'Channel 3')
    plt.xlabel('Granularity 10')
    plt.ylabel('Hz')
    plt.title(title)
    plt.legend(loc = 'center right')
    plt.savefig("./Plots/RAW/" + title + '.png')
    plt.clf()



def plotRawData():
  dataLocation = "./Recordings/SoftwareProject/"
  inputs = os.listdir(dataLocation)
  for input_ in inputs:
      # getting the name from the file name and removing numbers and extension from the name
      title = input_.split("-")[-1].split(".")[0].translate({ord(k): None for k in digits})
      plot_initial(input_ + '/', title)


plotRawData()