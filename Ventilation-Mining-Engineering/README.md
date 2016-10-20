**Ventilation Engineering Python Code for the Mining Engineering Industry**

The purpose of this repository is to collect python code developed by Joaquin Roibal during his Master's degree for use by Ventilation Engineers in the Mining Industry. Primary Implementation is using a Raspberry Pi Sensehat to collect and analyze ventilation data.

Short Description of files contained in this github repository:

"Meas_Test.csv" is formatted data recorded with raspberry pi sensehat for 4 days in a laboratory setting, "Meas_Test2.csv" is a similarly formatted collection of data from 10/15/2016-10/20/2016 in Socorro, NM

"Raspberry_Pi_data_display.py" will create a chart of variables collected with a sensehat, example is using Meas_Test.csv to visualize data, Includes Raspberry_Pi_data_Display2 & 3, which graph the data from Meas_Test2 and Meas_Test1, and 2 together.

"Table63_AltimeterLeapfrogging.csv" contains data which is used as an example program to evaluate the vent_python_toolbox program code

"VentSurveyProgram.py" is currently an outline for a OOP version of vent_python_toolbox, currently non-functional. Plans are in motion to format Ventilation Python Toolbox in OOP

"Ventilation_Mining_Python_Toolbox.py" **PRIMARY DOCUMENT** is a collection of functions useful for a ventilation engineer to calculate air properties in a mining environment. Can be imported and used in further python programs for ventilation engineers to develop their own tests/data collection. 

"sense_hat_specific_weight_data_collection.py" will record and collect data which can then be displayed with "Raspberry_Pi_Data_Display.py" python code. Records data every 5 minutes and 10 seconds, records into a CSV file. 

Read More About Ventilation Engineering at the Ventilation Engineering Wiki here: https://github.com/Roibal/Geotechnical_Engineering_Python_Code/wiki
