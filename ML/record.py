import time
import datetime
import sys
import random


outputLabels = []

def writeToFile():
    print("ATTEMPT WRITING TO FILE...")
    with open('actionTimeStamps.txt', 'w') as f:
        for item in outputLabels:
            f.write("%s\n" % item)
    print("WROTE TO FILE AND EXITED")

import sys, signal
def signal_handler(signal, frame):
    # print("\nprogram exiting gracefully")
    writeToFile()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

def main(argv):

    seconds = 120
    # parse second
    if (argv[0] == "--sec"):
        seconds = int(argv[1])
        print("RECORDING FOR " + str(seconds) + " SECONDS")
    else:
        print("RECORDING FOR DEFAULT" + str(seconds) + " SECONDS")
    start = datetime.datetime.now()

    while (datetime.datetime.now() - start).seconds < seconds:

        # print("Wait for prompt -- seconds elapsed:" , datetime.datetime.now() - start)
        secsToWaitBeforePromp = random.randint(5, 8)
        time.sleep(secsToWaitBeforePromp)
        print("PERFORM ACTION NOW -- elapsed:", datetime.datetime.now() - start)
        outputLabels.append(str(datetime.datetime.now().time()))
        time.sleep(3) #  wait 3 seconds to perform action


        
        
    writeToFile()

if __name__ == "__main__":
    try:
        main(sys.argv[1:])
    except KeyboardInterrupt:
        pass