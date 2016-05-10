import matplotlib.pyplot as plt
import numpy as np

def PillarDesign(sigma_z, pillar_width, room_width, height, design_fos):
    """
    The Purpose of this program is to successfully design pillar for room and
    pillar underground mining method based on example Measurements.
    Copyright Joaquin Roibal 2016
    New Mexico Institute of Mining and Technology
    """
    
    pillar_stress = PillarStress(sigma_z, pillar_width, room_width)
    ps = PillarStrength(height,pillar_width)
    factor_of_safety = FactorOfSafety(ps, pillar_stress)

    print("Original Pillar Stress: {}".format(pillar_stress))
    print("Calculated Pillar Strength: {}".format(ps))
    print("Factor of Safety of Original Design Requirements: {}".format(factor_of_safety))

    while factor_of_safety > design_fos:
        room_width += .1
        pillar_width -= .1
        ps = PillarStrength(height, pillar_width)
        pillar_stress = PillarStress(sigma_z, pillar_width, room_width)
        factor_of_safety = FactorOfSafety(ps, pillar_stress)
    print("Final Design Requirements for FOS = {}\nRoom Width: {} \nPillar Width: {}".format(factor_of_safety,
                                                                                          room_width, pillar_width))
    print("Pillar Strength: {}".format(ps))
    print("Extraction Ratio: {}".format(ExtractionRatio(pillar_width,room_width)))
    print("Extraction Ratio: {}".format(ExtractionRatio(pillar_width,room_width)))

    while factor_of_safety < design_fos:
        room_width -= .1
        pillar_width +=.1
        ps = PillarStrength(height,pillar_width)
        pillar_stress = PillarStress(sigma_z, pillar_width, room_width)
        factor_of_safety = FactorOfSafety(ps, pillar_stress)
    print("Final Design Requirements for FOS = {}\nRoom Width: {} \nPillar Width: {}".format(factor_of_safety,
                                                                                             room_width, pillar_width))
    print("Pillar Stress: {}".format(pillar_stress))
    print("Pillar Strength: {}".format(ps))
    print("Extraction Ratio: {}".format(ExtractionRatio(pillar_width,room_width)))

def PillarStrength(height, width):
    return 10.44*height**(-.7)*width**(0.5)

def FactorOfSafety(p_strength, p_stress):
    return p_strength/p_stress

def ExtractionRatio(pillar_width,room_width):
    return ((pillar_width+room_width)**2-(pillar_width**2))/((pillar_width+room_width)**2)

def PillarStress(sigma_z, pillar_width, room_width):
    return sigma_z*((pillar_width+room_width)/pillar_width)**2

def PlotExample():
    """
    Example Plot for varying Pillar, Room Widths which displays the
    Varying Extraction Ratios.
    """
    er = []
    wp = [x for x in range(1,15)]
    wo = [y for y in range(1,15)]
    for w_p in wp:
        w_open = []
        for w_o in wo:
            w_open.append(ExtractionRatio(w_p,w_o))
        er.append(w_open)
        plt.plot(wo, w_open, label = 'Pillar Length: {}'.format(w_p))    
    plt.xlabel('Width Opening of Tunnel')
    plt.ylabel('Extraction Ratio')
    plt.title('Extraction Ratio, Varying Room and Pillar Sizing')
    print(er)
    plt.legend(loc=4)
    
    plt.figure(2)
    er2 = []
    sigma_z = 3.375
    height = 3
    for w_p in wp:
        w_open2 = []
        for w_o in wo:
            pstress = PillarStress(sigma_z, w_p, w_o)
            pstrength = PillarStrength(height, w_p)
            FOS = FactorOfSafety(pstrength, pstress)
            w_open2.append(FOS)
        er2.append(w_open2)
        plt.plot(wo, w_open2, label = 'Pillar Length: {}'.format(w_p))
    plt.xlabel('Width Opening of Tunnel')
    plt.ylabel('Factor of Safety')
    plt.title('Factor of Safety, Varying Room and Pillar Sizing')
    plt.legend(loc=1)
    plt.show()

def main():
    depth = 150                             #Meters
    height = 3                              #Pillar Height in Meters
    gamma_rock = 22.5                       #kN/m^3
    pillar_width = 7                        #Meters
    room_width = 6                          #Meters
    sigma_z = depth * gamma_rock/1000
    design_fos = [1.3, 1.6]
    for fos in design_fos:
        PillarDesign(sigma_z, pillar_width, room_width, height, fos)

    PlotExample()

if __name__ == "__main__":
    main()
