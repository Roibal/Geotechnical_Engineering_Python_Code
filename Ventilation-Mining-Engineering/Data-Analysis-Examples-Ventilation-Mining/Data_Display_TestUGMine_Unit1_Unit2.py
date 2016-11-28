import matplotlib.pyplot as plt
import csv
import datetime 

"""
The Purpose of "Data_Display_TestUGMine.py" is to load data and display data
collected by the two data collection units (raspberry pi & sense Hat)
for the purpose of ventilation engineering. 

The Data collected in this example was collected over a period of two days at
an underground mining operation 

Created by: Joaquin Roibal

Copyright 2016 (c) Joaquin Roibal
All Rights Reserved
November 28, 2016

"""

def displaygraphs(measured_csv_file):
        #Create Lists to store values from CSV which will be used to graph values
    temp_list = []
    press_list = []
    datetime_list = []
    num_list = []
    humidity_list = []
        #Read in values from CSV
    first_recording = datetime.datetime.strptime("11/17/2016 06:00:00", "%m/%d/%Y %H:%M:%S")
    last_recording = datetime.datetime.strptime("11/18/2016 14:30:00", "%m/%d/%Y %H:%M:%S")
    with open(measured_csv_file, 'r') as csvfile:
        datareader = csv.reader(csvfile)
        for row in datareader:
            if row == []:
                pass
            else:
                print(row)
                num_list.append(row[0])     #Create List of Numbers 
                #Convert from imported csv format back into datetime object
                date = row[-2].strip(" ")
                time = row[-1].strip(" ")
                time_format = str(date + ' ' + time)
                dt = datetime.datetime.strptime(time_format, "%m/%d/%Y %H:%M:%S")
                print(dt)
                #Create a list of datetime objects
                datetime_list.append(dt)
                #create a list of temperature objects
                temp_list.append(float(row[1]))
                press_list.append(float(row[2]))
                humidity_list.append(float(row[-3]))
                if dt<first_recording or dt>last_recording:
                    datetime_list.pop()     # remove measured value if out of
                    temp_list.pop()         # desired time period
                    press_list.pop()
                    humidity_list.pop()
    """
    #Code Commented Out to develop new graph of specific weight/temp
        #Create SubPlots for specific weight and temperature
    plt.subplot(2, 1, 1)
    plt.plot(datetime_list, spec_weight_list)
    plt.title('Measurement of Specific Weight')
    plt.ylabel('Specific Weight, kg/m**3')

    plt.subplot(2, 1, 2)
    plt.plot(datetime_list, temp_list)
    plt.title('Measurement of Temperature')
    plt.ylabel('Temperature - Celcius')
    plt.show()
    """

    #Following Code is from Example 
    #http://matplotlib.org/examples/pylab_examples/multiple_yaxis_with_spines.html

    fig, host = plt.subplots()
    fig.subplots_adjust(right=0.75)
    
    par1 = host.twinx()
    par2 = host.twinx()
    par2.spines["right"].set_position(("axes", 1.2))
    make_patch_spines_invisible(par2)
    par2.spines["right"].set_visible(True)
    
    p1, = host.plot(datetime_list, humidity_list, "b-", label="Humidity")
    p2, = par1.plot(datetime_list, temp_list, "r-", label="Temperature")
    p3, = par2.plot(datetime_list, press_list, "g-", label="Pressure")

    host.set_title("Measurement and Recording of Temperature, Pressure, Humidity " +            measured_csv_file)
    host.set_xlabel("Time")
    host.set_ylabel("Relative Humidity (%)")
    par1.set_ylabel("Temperature (C) ")
    par2.set_ylabel("Pressure (kPa)")

    host.yaxis.label.set_color(p1.get_color())
    par1.yaxis.label.set_color(p2.get_color())
    par2.yaxis.label.set_color(p3.get_color())

    tkw = dict(size=4, width=1.5)
    host.tick_params(axis='y', colors=p1.get_color(), **tkw)
    par1.tick_params(axis='y', colors=p2.get_color(), **tkw)
    par2.tick_params(axis='y', colors=p3.get_color(), **tkw)
    host.tick_params(axis='x', **tkw)

    lines = [p1, p2, p3]
    host.legend(lines, [l.get_label() for l in lines])
    plt.show()

def make_patch_spines_invisible(ax):
    ax.set_frame_on(True)
    ax.patch.set_visible(False)
    for sp in ax.spines.values():
        sp.set_visible(False)

def main():
    meas_list = ['JR1_Data_Collect_TestMine.csv', 'JR2_Data_Collect_TestMine.csv']
    for files in meas_list:
        displaygraphs(files)

if __name__=="__main__":
    main()
