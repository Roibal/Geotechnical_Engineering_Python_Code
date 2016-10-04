import math

"""
The Purpose of this Program is to automate the task of Ventilation Surveying in Underground Mining Engineering.
This program can accept input of tabulated values (in csv file) for Leapfrogging and Roving-Base Altimeter
Indirect Method Surveys and provide data analysis and calculation output to a csv file.

Also provides many tools (Psychometric Properties of Air, Head Loss around Circuit, Specific Weight/Humidity Calc)
Analysis for Mine Ventilation Engineers.

pg 206, Mine Ventilation and Air Conditioning
Measured Values:
-Air Velocities (Vane Anemometer: v)
-Absolute and Differential Pressures or Heads (Manometer/Barometer/Altimeter: pb)
-Dry- and Wet-Bulb Temperatures (Thermometers: Tw, Td)
-Airway Dimensions (A)

Determine:
-Air Quantities
-Pressure Losses
-Air Specific Weights/Humidities
-Airway Resistance

Copyright Joaquin Roibal, August 2016, Latest Revision: 10/3/2016
All Rights Reserved
"""

def ManometerDirectMethod(TopList, BottomList, Manometer_Reading):
    """
    A Manometer is used to directly measure pressure difference (Direct Method).
    This function will perform the data analysis for Manometer Surveying given measured input values.
    Hl12 = (Hs1-Hs2)+(Hz1-Hz2)             #Head Loss (1->2) components
    Equations and Values from Example 6.3, page 208, Mine Ventilation and Air Conditioning Ramani and Wang
    """
    p3 = (BottomList[1] + (Manometer_Reading/27.69))  #Page 210, Pressure 3 = p2 + manometer reading (converted to psi)
    Ws = (TopList[-1]+BottomList[-1])/2               #Mean Specific Weight of Air in Hose
    Wh = (TopList[-1]+0.0705)/2                                  #Mean Specific Weight of Air in Shaft
    #Hl13 = (144*(Top[1]-p3)/5.2)+(Wh*(Top[0]-Bottom[0])/5.2)     #Page 209, Head Loss 1->3
    #Hl12 = (144*(Top[1]-Bottom[1])/5.2)+(Ws*(Top[0]-Bottom[0])/5.2) #Page 209, Head Loss 1 -> 2
    Hl12 = round((144/5.2)*(p3-BottomList[1])+(1/5.2)*(TopList[0]-BottomList[0])*(Ws-Wh), 3)
    return "Manometer Survey Results:\nWs: %s, Wh: %s, Head Loss in. Water: %s" %(Ws, Wh, Hl12)

def CalculateFrictionFactor(head_loss_f, length, diameter, quantity, spec_weight_air=0.075):
    """
    The Purpose of this function is to calculate the friction factor of an airway/ducting given parameters
    Utilizes Darcy-Weisbach equation and Atkinson Equation, 5.20 page 153 Mine Ventilation and Air Conditioning 3rd Edition
    """
    duct_perimeter = 2 * 3.14159 * (diameter / 2)
    area_opening = 3.14159 * (diameter / 2)**2
    rubbing_surface = length * duct_perimeter
    friction_factor_k = (spec_weight_air/0.075) * (head_loss_f*5.2*area_opening**3) / (duct_perimeter * length * quantity**2)
    return friction_factor_k
    
def NaturalVentilation(ShaftATop, ShaftABottom, ShaftBTop, ShaftBBottom):
    """
    The purpose of this function is to calculate the Natural Ventilation Head in Inches Water Gage.
    Inputs required: Lists in the following format: [DryBulbTemp, WetBulbTemp, Elevation, Pressure (in Hg)
    Method 2, page 297 in Ramani "Mine Ventilation And Air Conditioning" is used in commented example
    Equation used is from ME 440: Mine Ventilation with Dr. Bhattacharyya, ignoring vapor pressure
    :param ShaftATop:
    :param ShaftABottom:
    :param ShaftBTop:
    :param ShaftBBottom:
    :return:
    """
    """
    This Section is Commented Out Because NOT WORKING: Alternative Method Below
    spec_weight_air_shaft_a_top = psychrometricPropAir(ShaftATop[0], ShaftATop[1], ShaftATop[3])
    spec_weight_air_shaft_a_bottom = psychrometricPropAir(ShaftABottom[0], ShaftABottom[1], ShaftABottom[3])
    spec_weight_air_avg_upcast = (spec_weight_air_shaft_a_top[8] + spec_weight_air_shaft_a_bottom[8])/2
    spec_weight_air_shaft_b_top = psychrometricPropAir(ShaftBTop[0], ShaftBTop[1], ShaftBTop[3])
    spec_weight_air_shaft_b_bottom = psychrometricPropAir(ShaftBBottom[0], ShaftBBottom[1], ShaftBBottom[3])
    spec_weight_air_avg_downcast = (spec_weight_air_shaft_b_top[8] + spec_weight_air_shaft_b_bottom[8])/2
    L = ShaftBTop[2]-ShaftATop[2]
    print(L)
    print("Specific Weight Air Top A: ", spec_weight_air_shaft_a_top[9])
    print("Specific Weight Air Bottom A: ", spec_weight_air_shaft_a_bottom[9])
    print("Avg Spec Weight Upcast: ", spec_weight_air_avg_upcast)
    print("Avg Spec Weight Downcast: ", spec_weight_air_avg_downcast)
    inches_water_gage = (L/5.2)*(spec_weight_air_avg_downcast-spec_weight_air_avg_upcast)
    return inches_water_gage
    """
    
    #The Following Method Utilizes the equation from ME 440: Mine Ventilation by Dr. Bhattacharyya
    #NOTE: IGNORES VAPOR PRESSURE

    density_air_shaft_a_top = round((1.327/(460+ShaftATop[0]))*ShaftATop[-1], 6)
    print("Density Air Shaft A Top: ", density_air_shaft_a_top)
    density_air_shaft_a_bottom = round((1.327/(460+ShaftABottom[0])*ShaftABottom[-1]), 6)
    print("Density Air Shaft A Bottom: ", density_air_shaft_a_bottom)
    density_air_shaft_b_top = round((1.327/(460+ShaftBTop[0])*ShaftBTop[-1]), 6)
    print("Density Air Shaft B Top: ", density_air_shaft_b_top)
    density_air_shaft_b_bottom = round((1.327/(460+ShaftBBottom[0])*ShaftBBottom[-1]), 6)
    print("Density Air Shaft B Bottom: ", density_air_shaft_b_bottom)
    density_avg_shaft_a = (density_air_shaft_a_bottom + density_air_shaft_a_top)/2
    density_avg_shaft_b = (density_air_shaft_b_bottom + density_air_shaft_b_top)/2

    pressure_diff = round(abs((density_avg_shaft_a - density_avg_shaft_b)), 6)
    elevation_diff = (ShaftBTop[-2]-ShaftABottom[-2])
    print("Pressure Difference: ", pressure_diff)
    print("Elevation Difference: ", elevation_diff)
    inches_water_gage = round((pressure_diff*elevation_diff)/5.2, 4)
    return inches_water_gage

def psychrometricPropAir(td, tw, pb):
    """
    The purpose of this function is to accept input of measured values (wet-bulb, dry-bulb temp, barometric pressure)
    to calculate the Psychrometric properties of Air (Spec Weight)and return a list of values calculated:
    Ps, Ps Prime, Pv, Phi, W, Ws, Mu, Pa, V, w, h . Will be used in other functions to calculate head loss, etc.

    Example Values and Equations from Page 13, Mine Ventilation And Air Conditioning Textbook by Ramani and Wang
    :param td: Dry Bulb Temperature
    :param tw: Wet Bulb Temperature
    :param pb: Pressure (in Hg)
    :return:
    """
    Td = (td + 459.67)       #Convert Temperature from Fahrenheit to Kelvin
    val_list = [td, Td, tw, pb]       #List of Values to be returned by function,
                        #Final Format for List: [td, Td, tw, pb, ps, ps_prime, pv, phi, W, Ws, mu, pa, v, w, h]

    m = 28.97           #Molecular Weight
    s = 1               #Specific Gravity
    R = 53.35           #ft*lb/lb mass*Degree Rankine, Gas Constant
    w = 0.0750          #lb/ft^3, Specific Weight at Standard Conditions
    standard_pb = 29.92 #in. Hg, Standard Barometric Pressure at Sea Level
    cp = 0.2403         #Btu/lb*degreeF, Specific Heat at Constant Pressure
    cv = 0.1714         #Btu/lb*degreeF, Specific Heat at Constant Volume
    gamma = 1.402       #Ratio of Spec heats at constant pressure and volume for diatomic gas


            #Calculate Saturation Vapor Pressures: (Page 15, Mine Ventilation and Air Conditioning)
    ps = 0.18079*math.exp((17.27*td-552.64)/(td+395.14))      #in. Hg, Saturation Vapor Pressure, Dry Bulb Temp, eq 2.2
    val_list.append(ps)
    ps_prime = 0.18079*math.exp((17.27*tw-552.64)/(tw+395.14))  #in. Hg, Saturation Vapor Pressure, Wet Bulb Temp
    val_list.append(ps_prime)

    pv = ps_prime - ((pb-ps_prime)*(td-tw))/(2800-1.3*tw)       #in. Hg, Partial Pressure of Water Vapor in Air, eq. 2.3
    val_list.append(pv)
    phi = pv/ps*100                         #Relative Humidity, eq. 2.4
    val_list.append(phi)

    W = 0.622*pv/(pb-pv)      #lb/lb dry air, Specific Humidity, Eq. 2.5
    val_list.append(W)
    W_grain = W*7000            #grains/lb dry air
    Ws = 0.622*ps/(pb-ps)       #lb/lb wet air, Specific Humidity, Eq. 2.5 (Wet Bulb Temp)
    val_list.append(Ws)
    Ws_grain = Ws*7000          #grains/lb wet air

    mu = W/Ws*100               #Degree of Saturation, eq 2.6
    val_list.append(mu)

    pa = pb-pv              #in Hg, Pressure of Dry Air
    val_list.append(pa)

    v = (R*Td)/(pa*0.491*144)     #ft**3/lb dry air, Specific Volume (volume per unit weight of dry air), eq. 2.7
    val_list.append(v)
    w = (1/v)*(W+1)         #lb/ft**3, Specific Weight of Moist air or Mixture, eq. 2.8
    val_list.append(w)

    #w1 = (1.325/Td)*(pb-0.378*pv_prime)        #Alt Method for Calculating Spec. Weight. pv_prime unknown (?), eq. 2.9

    #h =ha+hv = cp*td+W*(hfg+hf)        #Enthalpy, total heat content of Air
    h = cp*td+W*(1060+0.45*td)        #Btu/lb dry air, Enthalpy, eq. 2.10
    val_list.append(h)
    return val_list

def PressureSurveyCalc(pa2, pa1, pb2, pb1, pb, td, pv_prime, Z2, Z1, V2, V1):
    """
    The Pressure Survey Calc function will perform the calculations required for Indirect Method of
    Ventilation Survey (Leapfrogging Method, Roving-Base Altimeter), including:
    -Head Loss
    :return:
    """
    w1, w2 = 0.0750, 0.0750             #Assumed Values for specific weight, Page 217
    CF = 69              #Conversion Factor Assumed to be 69 ft of air column = 1 inch Water (Example 6.5)
    DR = 1      #((1.325/(460+50))*pb) / ((1.325/(460+td))*(pb-0.378*pv_prime))     #Density Ratio, Eq 6.13 page 216
    #HL21 = (H2 - H1) + (Ha2-Ha1) + (Hv2-Hv1) + (Hz2-Hz1)       Head Loss Equation, Eq 6.11
    HL21 = -((pa2-pa1)-(pb2-pb1)-(Z2-Z1)/DR)/CF + (V2**2-V1**2)/(4009**2)  #Calculate Head Loss Based on Altimeter
                                                #Units, Elevation and Temperature, Equation 6.12 Page 216
    Hv21 = ((V2**2-V1**2)/(4009**2))*(((w1+w2)/2)/0.0750)           #Velocity Head, Eq 6.14
    return [HL21, Hv21, DR, CF]

def RovingBaseAltimeter(measurement_list):
    """
    Roving Base Altimeter Function will accept inputted list of measured values and output a formatted table of
    calculated results. Formatting Based on Example 6.6 page 222-223 in Mine Ventilation and Air Conditioning.
    Input Format: Stat - Location - I/R - Elev (ft) - Time - RAR, ft - WetBulb T - DryBulb T - Velocity (fpm) - BAR, ft
    Output Format: Stat - Phi - Hv in Water - Diff Elev - DR - Alt Diff - Base Corr. - Elev. Corr. - Head ft Air - (cont)
        - Avg Alt Reading - Feet of Air per in Water - Delta Hs - Delta Hv - Delta Ht - Ht
    :param measurement_list:
    :return:
    """
    Altimeter_Vent_Survey_Table = []
    for measurement in measurement_list:
        results_table = []              #Create Empty List which will be used to append calculated values in table format
        air_prop_list = psychrometricPropAir(measurement[6], measurement[7], measurement[9])    #Calculate Psychometric Prop
        results_table.append(measurement[0])                #Append Station Number
        results_table.append(air_prop_list[7])          #Append Relative Humidity % (Phi) from Psychometric Prop List
        #[Hl, Hv, DR, CF] = PressureSurveyCalc()                #Retrieve Velocity Head Values from PressureSurveyCalc
        #results_table.append(Hv)                        #Append Velocity Head Values to Results Table
        #results_table.append(Elev_Diff)                 #Append Elevation Difference to Results Table
        #results_table.append(DR)                        #Append DR from Pressure Survey Calc function
        #Altimeter_Diff = measurement[5]-Prev_Altimeter  #Calculate Altimeter Difference from Previous Altimeter Value
        #results_table.append(Altimeter_Diff)            #Append Calculated Altimeter Difference Value to Results Table
        #results_table.append(Base_Correct)              #Append Base Correction
        #results_table.append(Elev_Correct)              #Append Elevation Correction
        #results_table.append(HeadFtOfAir)               #Append Head Feet of Air
        #results_table.append(AvgAltReading)
        #results_table.append(CF)
        #results_table.append(DeltaHs)                   #All Head in in H20
        #results_table.append(DeltaHv)
        #results_table.append(DeltaHt)
        #results_table.append(Ht)
        Altimeter_Vent_Survey_Table.append(results_table)   #Append Results Table as One Line in Altimeter Vent Survey Table
    return Altimeter_Vent_Survey_Table

def LeapfroggingAltimeter(User_List ="Table63_AltimeterLeapfrogging.csv" ):
    """
    Leap Frog Altimeter is a Function To Determine Values for a Leapfrogging Altimeter Ventilation Survey.
    Accepts Input in csv format and returns a list of calculated values in format:
    - Hl (Head Loss) - Hv (Head Loss due to Velocity) - DR (Density Ratio) - CF (Conversion Factor, ft air per in water)
    Uses Example 6.5 page 220 as example to verify process
    :param User_List:
    :return:
    """
    Vent_list_leapfrog = LoadVentDataLeapfrog(User_List, [])
    print(Vent_list_leapfrog)
    Results_List = []       #Create Empty List to return Results Table of Calculated Values for Leapfrog Altimeter Surv
    for vent in Vent_list_leapfrog:
        line_list = []      #Create Empty List for each vent point
        line_list.append(str(vent[0]) + "-" + str(vent[1]))     #Display Stations
        line_list.append(int(vent[4])-int(vent[5]))             #Calculate Altimeter Difference
        line_list.append(int(vent[2])-int(vent[3]))             #Calculate and Append Elevation Difference
        [Hl, Hv, DR, CF] = PressureSurveyCalc(int(vent[4]), int(vent[5]), 0, 0, 0, 0, 0, int(vent[2]),
                                            int(vent[3]), int(vent[-2]), int(vent[-1]))
        line_list.append(Hl)        #Calculate Head Loss
        air_flow = ((int(vent[-1])+int(vent[-2]))/2)*((float(vent[-4])+float(vent[-3]))/2)      #Calculate
        line_list.append(air_flow)
        Results_List.append(line_list)
    print(Results_List)


def LoadVentDataLeapfrog(vent_data_csv, vent_data_list):
    #This Function Will Load Vent Data from a CSV file and send to AddVentData Function to create a list of dicts
    with open(vent_data_csv, 'r') as vent_file:
        i = 0
        for line in vent_file:
            new_line = line.split(',')
            if i<3:         #Skip first two lines of CSV file due to headings
                i += 1
                pass
            else:
                vent_data_list.append([new_line[0], new_line[1], new_line[2], new_line[3], new_line[4], new_line[5],
                    new_line[6], new_line[7], new_line[8], new_line[9], new_line[10], new_line[11],
                    new_line[12], new_line[13].strip("\n")])        #Create List of Formatted CSV Values
    return vent_data_list

def HeadLossCurcuit(List_Head):
    """
    Head Loss Circuit is a function which calculates the head loss around a closed ventilation circuit.
    Accepts input of a list (Junctions From-To) and Head Losses, in Water
    A closed-circuit head loss is calculate and returned as a percentage (%)
    Returns a Tuple of (Head Loss Error, Error Percentage)
    """
    HeadLossVal = 0         #Set Initial Head Loss to 0
    TotalHeadLoss = min(List_Head)       #Total Head Loss Determined by Lowest Press. Measurement, Error Percentage (%)
    for HeadLoss in List_Head:
        HeadLossVal += HeadLoss         #All Values are summed to determine closure error of circuit
    #print(TotalHeadLoss)
    percentage_error = round(abs(HeadLossVal)/abs(TotalHeadLoss)*100, 2)
    print("Error Percentage of Head Loss Circuit:", percentage_error)
    return (round(HeadLossVal, 3), percentage_error)

def main():
    """
    Examples and Solutions based on Mine Ventilation and Air Conditioning Textbook to
    demonstrate the proper usage of functions and verify process and Data Analysis.
    :return:
    """
    #An example of direct method of pressure measurement with Manometer
    #Key = [Elevation (ft), Pressure (psi), Temp (Dry Bulb F), Temp (Wet Bulb F), Spec Humid, Spec Weight]
    Top = [-1748.7, 12.594, 59.4, 50, 0.0072, 0.0655]
    Bottom = [-4368.70, 13.773, 67.3, 57,0, 0.0082, 0.0702]
    Manometer_Reading = 1.51                                #Inches of Water
    print(ManometerDirectMethod(Top, Bottom, Manometer_Reading))      #Page 209/210 Example Mine Ventilation Textbook

    print(psychrometricPropAir(70, 50, 29.921))         #Example 2.1 from Mine Ventilation and Air Conditioning, Page 17

    list_of_head = [.445, 1.075, -8.6, 0.245, 2.8, 0.19, 0.084, 0.455, 1.50, 1.71]  #Example 6.4 pg 211 Mine Ventilation
    print("Head Loss in in H20: ", HeadLossCurcuit(list_of_head))
    LeapfroggingAltimeter()
    
    #An Example of Natural Ventilation Head in Inches Water, Example from Dr. Bhattacharyya ME 440 HW #1
    ShaftATop = [63, 63, 1000, 28.95]
    ShaftABottom = [65, 65, 300, 29.80]
    ShaftBTop = [67, 59, 1200, 28.75]
    ShaftBBottom = [59, 53, 500, 29.60]
    NaturalVent = NaturalVentilation(ShaftATop, ShaftABottom, ShaftBTop, ShaftBBottom)
    print(NaturalVent)
    
    #An Example 5.6, page 159 Ramani, Wang, Mutmansky and Hartman to calculate friction factor
    frict_factor_k = CalculateFrictionFactor(21.04, 3000, 4, 48000, 0.075)
    print("Example 5.6, Friction Factor K: ", frict_factor_k)

if __name__ == "__main__":
    main()
