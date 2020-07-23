import readData as rd
import fourier as ft

dataLocation = "Recordings/SoftwareProject/"
print(rd.getFileLocs(dataLocation))

channel_0_x, channel_0_y = rd.getData('OpenBCISession_2020-04-25_15-29-52-eyeblink', None, 0, None)

fft = ft.fftData(channel_0_x, channel_0_y, None)
print(len(fft[1]))



# SO WHAT WE WANT TO DO TODAY:
# WE have functions to read data and create fourier transforms
# Let's take our input data stream and split it into 5 second intervals, and create a fourier trasnform of all of those. Then do that for each channel of the data. 
# def getObservations(fileName):

#   return observations,labels