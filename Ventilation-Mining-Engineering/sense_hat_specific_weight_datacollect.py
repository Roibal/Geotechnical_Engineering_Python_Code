import math
from sense_hat import SenseHat
#import matplotlib
import datetime
import time as time2

sense = SenseHat()		#create sensehat object

"""
The purpose of this program is to accept input from Raspberry pi sense hat
and calculate and display specific weight of air on LED matrix. Units are in metric.
Copyright Joaquin Roibal, June 2016, All Rights Reserved 
Latest Modification: October 2016
Description: Added Data Collection Module which will record in a csv file
"""

def main():
	while 1:			#Create Infinite Loop to accept input, calc values, reloads after LED completes message
		R = 287.045					#Ideal Gas Constant, J/kg*K 
		t = round(sense.get_temperature(),2)		#Celcius - Dry bulb temp
		abs_t = t+ 273					#convert Temp from Celcius to Kelvin
		p = round(sense.get_pressure(),2)		#Millibars with 2 decimals of accuracy
		p = 0.1*p					#Convert to kPa from millibars (kPa)
		h = round(sense.get_humidity(),1)		#Relative Humidity
		tw = t*math.atan((0.151977*(h+8.313659)**(1/2)))+math.atan(t+h)-math.atan(h-1.676331)+0.00391838*h**(3/2)*math.atan(0.023101*h)-4.686035
               		#Above equation used to convert dry bulb temp and relative humidity to wet_bulb
		tw = round(tw,1)
		msg = "Temp (Celcius): %s, Wet Bulb: %s, Pressure: %s kPa, Humidity: %s percent. rel. humid." %(t, tw, p, h)
		ps = round(0.6105*math.exp((17.27 * t)/(t+237.3)), 2)		#kPa for vapor pressure, pg 15 Mine Vent. 
		ps_prime = round(0.6105*math.exp((17.27*tw)/(tw+237.3)), 2)	#kPa vapor pressure wet bulb
		pv = round(ps_prime - 0.000644*p*(t-tw), 2)			#Calculate Vapor Pressure 
		msg += "Sat Vapor Pressure: %s , ps_prime: %s , pv: %s" %(ps, ps_prime, pv)	#Append values to 'msg'
		spec_humidity = round((0.622 * pv)/(p-pv), 2)			#kg/kg
		spec_humidity_s = round((0.622*ps)/(p-ps), 2) 			#spec humidity kg/kg at tw
		spec_volume = round((R*abs_t)/((p-pv)*1000), 2)			#(m**3/kg)
		print("Specific Humidity: %s , Specific Volume: %s, Ws: %s" %(spec_humidity, spec_volume, spec_humidity_s))
		spec_weight1 = round((1/spec_volume)*(spec_humidity+1), 4)	#Calculate Specific Weight
		spec_weight = round((1/(0.287*abs_t))*(p-0.378*pv), 4)		#kg/m**3, eq. 7 pg 16, Mine Vent
		msg += "Spec Weight: %s, Spec Weight 2: %s" %( spec_weight, spec_weight1)
		#sense.show_message(msg, scroll_speed = 0.05)		#Possible to show values on LED
		print(msg)						#Print All Calculated Values to screen
		
        
		time = datetime.datetime.now()

		for attr in ['year', 'month', 'day', 'hour', 'minute', 'second', 'microsecond']:
			print(attr, ':', getattr(time, attr))
	
		data =[spec_weight, t, p, h, time]
		print(data)
		with open('Meas_Test.csv', 'a') as f:
			f.write(str(data)+ "\n")
		sense.show_message(str(spec_weight)+" kg/m**3")		#Display specific weight on sense_hat LED matrix
		#dataCollectStore("meas_test.csv")
		time2.sleep(300)		#Record one value every 5 minutes (slightly more due to delay of LED Matrix-will fix)

def dataCollectStore(input_file, measure_interval=180):
	"""
	The purpose of this function is to collect and store data from Sense Hat including time stamp and 
	creating a file with measured values
	"""
	t = round(sense.get_temperature(),2)		#Celcius - Dry bulb temp
	p = round(sense.get_pressure(),2)		#Millibars with 2 decimals of accuracy
	p = 0.1*p					#Convert to kPa from millibars (kPa)
	h = round(sense.get_humidity(),1)		#Relative Humidity
	#today = datetime.date.today()
	time = datetime.datetime.now()

	for attr in ['year', 'month', 'day', 'hour', 'minute', 'second', 'microsecond']:
		print(attr, ':', getattr(time, attr))
	
	data =[t, p, h, time.year, time.month, time.day, time.hour, time.minute, time.second]
	print(data)

if __name__=="__main__":
    main()
