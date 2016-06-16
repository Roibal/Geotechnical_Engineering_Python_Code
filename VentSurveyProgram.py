class VentilationSurvey(object):

    """
    The purpose of this program is to automate the data analysis portion of a ventilation survey performed in
     an underground mine. Accepts a .csv of input parameters from a ventilation survey data (see format) which
     is then used to calculate relevant parameters of ventilation survey.

     Main Resource is "Mine Ventilation And Air Conditioning" 3rd Edition by Mutmanskiy, Hartman, Ramani & Wang.

     Coded 5/8/2016 by Joaquin Roibal
     Copyright 2016
     All Rights Reserved
    """

    def __init__(self, name="Example Mine Vent Survey 1"):
        self.name = name
        self.vent_points = []      #A Blank List is created and will store dictionaries of each data point
        print("Welcome to the Mine Ventilation Survey Python Toolbox written by Joaquin Roibal\n")

    def __str__(self):
        for item in self.vent_points:
            print(item)

    def ManometerSurvey(self, position, elevation, pressure, drybulbf, wetbulbf):
        """Example 6.3, page 208, mine ventilation and air conditioning example
        A Manometer is used to calculate pressure difference (Direct Method).
        """
        #Hl12 = (Hs1-Hs2)+(Hz1-Hz2)             #Head Loss (1->2) components
        Z1 = 1
        Z2 = 2
        p2 = 13.773
        p3 = (13.773 + (1.51/27.69))            #Page 210, Pressure 3 = p2 + manometer reading (converted to psi)
        Hl12 = (144/5.2)*(p3-p2)+(1/5.2)*(Z1-Z2)*(Ws-Wh)

    def Mod_AddData(self, station_no, desc, time_r, rar, time_b, bar, alt_diff, change_alt, feet_air, head, abs_head):
        if station_no.isalpha():
            #Feature will be added that for loops through 1st entered line and names the following dictionary
            #from the values of first column
            pass
        else:        self.vent_points.append({"Station Number": int(station_no),
                                  "Description": str(desc),
                                  "Time RAR": time_r,
                                  "Roving Altimeter Reading": float(rar),
                                  "Time BAR": time_b,
                                  "Base Altimeter Reading": float(bar),
                                  "Altitude Difference": change_alt,
                                  "Feet of Air": feet_air,
                                  "Inches of Water (Head)": head,
                                  "Absolute Head": abs_head.strip()})

    def LoadData(self, loadfile = "VentSurveyData.csv"):
        with open(loadfile, 'r') as file1:
            for line1 in file1:
                data = line1.split(',')
                self.Mod_AddData(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9],
                             data[10])

    def List(self):
        for item in self.vent_points:
            print(item)

    def SpecWeightAir(self):
        #method will be added which calculates the Specific Weight of Air which is used to calculate the proper head
        #based upon Dry Bulb Temperature and Wet Bulb Temperature
        pass

    def ConvertHead(self):
        #convert Specific Weight to Inches of Head in Water
        pass

    def PressureChange(self):
        pass

    def SaveList(self):
        pass

def main():
    ExampleMine = VentilationSurvey()
    ExampleMine.LoadData()
    ExampleMine.List()
    while 1:
            action = input("What would you like to do? Options: Add Data (A), Load Data (L), List Data (LD), Save (S)")
            if len(action)>1:
                pass
    print(ExampleMine.name)

if __name__=="__main__":
    main()
