def PillarDesign(sigma_z, pillar_width, room_width, height, design_fos):
    """
    The Purpose of this program is to successfully design pillar based on example Measurements.
    Copyright Joaquin Roibal 2016
    New Mexico Institute of Mining and Technology
    :return:
    """
    pillar_stress = sigma_z*((pillar_width+room_width)/pillar_width)**2
    ps = PillarStrength(height,pillar_width)
    factor_of_safety = ps/pillar_stress
    print("Original Pillar Stress: {}".format(pillar_stress))
    print("Calculated Pillar Strength: {}".format(ps))
    print("Factor of Safety of Original Design Requirements: {}".format(factor_of_safety))

    while factor_of_safety > design_fos:
        room_width += .1
        pillar_width -= .1
        ps = PillarStrength(height, pillar_width)
        pillar_stress = sigma_z*((pillar_width+room_width)/pillar_width)**2
        factor_of_safety = ps/pillar_stress
    print("Final Design Requirements for FOS = {}\nRoom Width: {} \nPillar Width: {}".format(factor_of_safety,
                                                                                             room_width, pillar_width))
    print("Pillar Strength: {}".format(ps))
    print("Extraction Ratio: {}".format(ExtractionRatio(pillar_width,room_width)))
    print("Extraction Ratio: {}".format(ExtractionRatio(pillar_width,room_width)))

    while factor_of_safety < design_fos:
        room_width -= .1
        pillar_width +=.1
        ps = PillarStrength(height,pillar_width)
        pillar_stress = sigma_z*((pillar_width+room_width)/pillar_width)**2
        factor_of_safety = ps/pillar_stress
    print("Final Design Requirements for FOS = {}\nRoom Width: {} \nPillar Width: {}".format(factor_of_safety,
                                                                                             room_width, pillar_width))
    print("Pillar Stress: {}".format(pillar_stress))
    print("Pillar Strength: {}".format(ps))
    print("Extraction Ratio: {}".format(ExtractionRatio(pillar_width,room_width)))

def PillarStrength(height, width):
    return 10.44*height**(-.7)*width**(0.5)

def ExtractionRatio(pillar_width,room_width):
    return ((pillar_width+room_width)**2-(pillar_width**2))/((pillar_width+room_width)**2)

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

if __name__ == "__main__":
    main()
