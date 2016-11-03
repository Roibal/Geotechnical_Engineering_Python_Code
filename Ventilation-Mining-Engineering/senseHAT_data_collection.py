import math
from sense_hat import SenseHat
import datetime
import time as time2

"""
The purpose of this program is to collect and record sensor input from Raspberry pi Sense hHAT
and calculate specific weight of air for Ventilation Engineering in Underground Mining.
Units are in metric.
Copyright 2016 Joaquin Roibal, All Rights Reserved
Latest Modification: November 2016
Description of Modification: Added Data Collection Module which will record in a csv file
Each Raspberry Pi Module should have 3 digit code which will be used to Identify
"""


def main():
    i = 0                           #Create Counter for Number of Measurements
    sense = SenseHat()		        #create sensehat object
    while 1:			    #Create Infinite Loop to accept measured values
        i += 1
        t = round(sense.get_temperature(),2)		#Celcius - Dry bulb temp
        #abs_t = t+ 273					#convert Temp from Celcius to Kelvin
        p = round(sense.get_pressure(),2)		#Millibars with 2 decimals of accuracy
        p = 0.1*p					#Convert to kPa from millibars (kPa)
        h = round(sense.get_humidity(),1)		#Relative Humidity
        time = datetime.datetime.now()
        data =[i, t, p, h, time]
        print(data)
        dataCollectStore(i, t, p, h)

def dataCollectStore(i, t, tw, p, h, spec_weight, input_file='JR1_Data_Collect.csv', sleep_interval=5):
    """
    The purpose of this function is to collect and store data from Sense Hat including time stamp and
    creating a file with measured values
    Name of Files to be changed for each Raspberry Pi [3/4 Digit Key] Data Collection with Sense HAT.
    """
    time = datetime.datetime.now()
    time_list = str(time.month)+"/"+str(time.day)+"/"+str(time.year)+" , "+str(time.hour)+":"+str(time.minute)+":"+str(time.second)

    with open(input_file, 'a') as f:
        #Data will be written to a file in the format [i, t, tw, p, h, spec_weight] and time
        f.write(str(i)+","+str(t)+","+str(tw)+","+str(p)+","+str(h)+","+str(spec_weight)+" , "+ time_list + "\n")

    time2.sleep(sleep_interval)		#One Value Recorded for each loop, sleep interval determines pause in seconds

if __name__=="__main__":
    main()
