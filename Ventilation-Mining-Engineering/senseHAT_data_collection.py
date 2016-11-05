import math
from sense_hat import SenseHat
import datetime
import time as time2

"""
The purpose of this program is to collect and record sensor input from Raspberry pi Sense HAT. Data is stored in a Microsoft Excel compatible
csv format file. Recording frequency can be adjusted. Units are in metric.
Further improvements will include the calculation of specific weight of air for Ventilation Engineering in Underground Mining.
Copyright (c) 2016 Joaquin Roibal, All Rights Reserved
Latest Modification: November 2016
Description of Modification: Added Data Collection Module which will record in a csv file
Each Raspberry Pi Module should have 3 digit code which will be used to Identify itself, can be added to Raspberry Pi Library
"""


def main():
    """
    Main Function to begin collecting and recording data from Raspberry Pi Sense HAT.
    Initializes an 'i' value (counter) each time the script is started, used to number data collections, calls 
    'dataCollectStore' an infinite amount of times with a rest between each recorded point.
    """
    i = 0                           #Create Counter for Number of Measurements
    sense = SenseHat()		        #create sensehat object
    while 1:			    #Create Infinite Loop to accept measured values        
        i += 1              #add 1 for each iteration then send this value to dataCollectStore function
        dataCollectStore(i)
                  
def dataCollectStore(i, input_file='ABC_Data_Collect.csv', sleep_interval=300):
    """
    The purpose of this function is to collect and store data from Sense Hat including time stamp and
    creating a file with measured values
    Name of Files to be changed for each Raspberry Pi [3/4 Digit Key] Data Collection with Sense HAT.
    """
    t = round(sense.get_temperature(),2)		        #Celcius - Dry bulb temp - UNCALIBRATED
    #abs_t = t+ 273					                    #convert Temp from Celcius to Kelvin
    p = round(sense.get_pressure(),2)		            #Millibars with 2 decimals of accuracy - UNCALIBRATED
    p = 0.1*p					                        #Convert to kPa from millibars (kPa) - UNCALIBRATED
    h = round(sense.get_humidity(),1)		            #Relative Humidity - UNCALIBRATED
    time = datetime.datetime.now()                      #Record time of measurement based on Raspberry Pi Internal Clock
    time_list = str(time.month)+"/"+str(time.day)+"/"+str(time.year)+" , "+str(time.hour)+":"+str(time.minute)+":"+str(time.second)
    data =[i, t, p, h, time_list]
    print(data)
    with open(input_file, 'a') as f:
        #Data will be written to a csv file in the format [ i, t, p, h, and time in format MM/DD/YYYY , HH:MM:SS ]
        #Input File is specified in dataCollectStore function , csv based on 3-Digit identifier for particular Raspberry Pi/sense HAT
        f.write(str(i)+","+str(t)+","+str(p)+","+str(h)+" , "+ time_list + "\n")

    time2.sleep(sleep_interval)		#One Value Recorded for each loop, sleep interval determines pause in seconds

if __name__=="__main__":
    main()
