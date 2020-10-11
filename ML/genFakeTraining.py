import readData as rd
import fourier as ft


dataLocation = "Recordings/SoftwareProject/"
print(rd.getFileLocs(dataLocation))

"""
Take the input dataset we have and generates a bunch of random noise for the observation we have, and also generates a bunch of 
"""
def genTrainingData():
    channel_0_x, channel_0_y = rd.getData('OpenBCISession_2020-04-25_15-29-52-eyeblink', None, 0, None)
    fft = ft.fftData(channel_0_x, channel_0_y, None)

    # eyeblink has 7108 samples
    # 15:35:25 -> 15:31:00