import math
import numpy
import matplotlib.pyplot as plt

def uni_comp_strength(c, Phi):
    """
    calculates and returns the Uniaxial Compressive Strength of the rock given Cohesion (c) and Friction Angle (Phi).
    """
    return (2*c*math.cos(math.radians(Phi)))/(1-math.sin(math.radians(Phi)))

def critical_pressure(Po, uni_comp_str, k):
    """
    Calculates and returns the critical pressure given Uniaxial Compressive Strength, Pressure (Vertical/Overburden), and k value.
    """
    return (2*Po-uni_comp_str)/(1+k)

def radius_plastic_zone(ro, Po, Pi, k, uni_comp_str):
    """
    Calculates and returns the radius of the plastic zone of the tunnel.
    """
    num = 2*(Po*(k-1)+uni_comp_str)
    denom = (1+k)*(k-1)*Pi+uni_comp_str
    return (ro*(num/denom)**(1/(k-1)))

def inward_radial_disp_plastic(ro, Po, crit_press, v, E, rp, Pi):
    """
    Calculates and returns the inward radial displacement for plastic analysis.
    """
    return (ro*(1+v)/E)*(2*(1-v)*(Po-crit_press)*(rp/ro)**2-(1-2*v)*(Po-Pi))

def main():
    E = 250000          #Young's Modulus
    v = 0.25            #Poisson's Ratio
    Po = 2500 * 1.1     #Vertical Pressure, Depth * 1.1 (Imperial Units - Feet)
    Phi = 32            #Friction Angle
    c = 800             #Cohesion
    Pi = 0              #Internal Pressure
    ro = 5              #Diameter of Circular Tunnel
    k = (1+math.sin(math.radians(Phi)))/(1-math.sin(math.radians(Phi))) #calculates k based on Phi (Friction Angle)
    print("The value of k : {}".format(k))
    uni_comp_str = uni_comp_strength(c,Phi)             #Calculates Uniaxial Compressive Strength
    crit_press = critical_pressure(Po, uni_comp_str, k)       #Determines Critical Pressure Pcr
    print("Critical Pressure: {} PSI".format(crit_press))
    Uie = (ro*(1+v)/E)*(Po-Pi)                                  #Elastic Displacement
    print("Maximum Elastic Displacement: {} feet".format(Uie))
                                                                    #Radius of Plastic Zone
    rp = radius_plastic_zone(ro, Po, Pi, k, uni_comp_str)
    print("Radius of Plastic Zone: {} feet".format(rp))
                                                                #Inward Displacement of Plastic Zone
    inward_disp_plastic = inward_radial_disp_plastic(ro,Po,crit_press,v,E,rp,Pi)
    print("Inward Displacement Plastic: {} feet".format(inward_disp_plastic))

    #Creating Characteristic Curve
    #For Loop which will adjust support pressure from In-Situ Stress Value to 0
    Ui = []
    Rp = []
    CharCurve = []
    displ_plast = []
    PiList = []

    Pi = Po
    i = 0
    while Pi>0:
        PiList.append(Pi)
        Pcr = critical_pressure(Po, uni_comp_str, k)    #Calc. Crit. Pressure
        i += 1
        Ui.append(i*0.05)
        
        if Pi>Pcr:              #If Internal Pressure > Critical Pressure, 
                                   # Elastic Deformation and Rp = ro
            Rp.append(ro)
            CharCurve.append((ro*(1+v)/E)*(Po-Pi))
        else:
            Rp.append(radius_plastic_zone(ro, Po, Pi, k, uni_comp_str))
            CharCurve.append(inward_radial_disp_plastic(ro,Po,Pcr,v,E,Rp[i-1],Pi))
        Pi -= 0.5
    
    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()
    ax1.plot(CharCurve, PiList, 'g-', label ="Characteristic Curve")
    ax1.plot([0,0.4], [Pcr, Pcr], 'r', label ="Critical Stress/Pressure")
    ax2.plot(CharCurve, Rp, 'b-', label="Radius of Plastic Zone")
    
    ax1.set_xlabel('Tunnel Wall Displacement')
    ax1.set_ylabel('Support Pressure', color='g')
    ax2.set_ylabel('Plastic Zone Radius', color='b')
    ax2.axis([0, 0.45, 0, 12])
    plt.legend()

    plt.show()

if __name__ == "__main__":
    main()
