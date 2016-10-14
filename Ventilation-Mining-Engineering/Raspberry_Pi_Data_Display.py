import matplotlib.pyplot as plt
import csv
import datetime 

"""
The Purpose of "Raspberry_Pi_Data_Display.py" is to load data and display data
collected by the raspberry pi for the purpose of ventilation engineering.

Created by: Joaquin Roibal, Copyright 2016
All Rights Reserved

"""


def displaygraphs(user_input='Meas_Test.csv'):
        #Create Lists to store values from CSV
    spec_weight_list = []
    temp_list = []
    press_list = []
    datetime_list = []
        #Read in values from CSV
    with open('Meas_Test.csv', 'r') as csvfile:
        datareader = csv.reader(csvfile)
        for row in datareader:
            if row == []:
                pass
            else:
                num = row[0].strip('[')
                spec_weight_list.append(float(num))     #Create List of Spec Weight
                    #Convert from imported csv format back into datetime object
                dt = datetime.datetime(int(2016), int(row[-6]), int(row[-5]), 
                    int(row[-4]), int(row[-3]), int(row[-2]))
                    #Create a list of datetime objects
                datetime_list.append(dt)
                    #create a list of temperature objects
                temp_list.append(float(row[1]))
                press_list.append(float(row[2]))
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
    
    p1, = host.plot(datetime_list, spec_weight_list, "b-", label="Specific Weight")
    p2, = par1.plot(datetime_list, temp_list, "r-", label="Temperature")
    p3, = par2.plot(datetime_list, press_list, "g-", label="Pressure")

    host.set_title("Measurement and Recording of Temperature, Pressure, Specific Weight")
    host.set_xlabel("Time")
    host.set_ylabel("Specific Weight (kg/m^3)")
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
    displaygraphs()

if __name__=="__main__":
    main()
