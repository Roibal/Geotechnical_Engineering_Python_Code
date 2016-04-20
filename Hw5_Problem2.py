import math
import numpy
import matplotlib.pyplot as plt

def uni_comp_strength(c, Phi):
    return (2*c*math.cos(math.radians(Phi)))/(1-math.sin(math.radians(Phi)))

def critical_pressure(Po, uni_comp_str, k):
    return (2*Po-uni_comp_str)/(1+k)

def radius_plastic_zone(ro, Po, Pi, k, uni_comp_str):
    num = 2*(Po*(k-1)+uni_comp_str)
    denom = (1+k)*(k-1)*Pi+uni_comp_str
    return (ro*(num/denom)**(1/(k-1)))

def inward_radial_disp_plastic(ro, Po, crit_press, v, E, rp, Pi):
    return (ro*(1+v)/E)*(2*(1-v)*(Po-crit_press)*(rp/ro)**2-(1-2*v)*(Po-Pi))

def main():
    E = 250000
    v = 0.25
    Po = 2500 * 1.1
    Phi = 32
    c = 800
    Pi = 0
    ro = 5
    k = (1+math.sin(math.radians(Phi)))/(1-math.sin(math.radians(Phi))) #calculates k
    print("The value of k : {}".format(k))
    uni_comp_str = uni_comp_strength(c,Phi)   #Calculates Uniaxial Compressive Strength
    crit_press = critical_pressure(Po, uni_comp_str, k)       #Determines Critical Pressure Pcr
    print("Critical Pressure: {} PSI".format(crit_press))
    Uie = (ro*(1+v)/E)*(Po-Pi)        #Elastic Displacement
    print("Maximum Elastic Displacement: {} feet".format(Uie))
    #Radius of Plastic Zone
    rp = radius_plastic_zone(ro, Po, Pi, k, uni_comp_str)
    print("Radius of Plastic Zone: {} feet".format(rp))
    #Inward Displacement of Plastic Zone
    inward_disp_plastic = inward_radial_disp_plastic(ro,Po,crit_press,v,E,rp,Pi)
    print("Inward Displacement Plastic: {} feet".format(inward_disp_plastic))

    #Creating Characteristic Curve
    #tunnel_wall_displacements = [j for j in range(0,inward_disp_plastic)]
    #print(tunnel_wall_displacements)

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
        CharCurve.append((ro*(1+v)/E)*(Po-Pi))
        if Pi>Pcr:              #If Internal Pressure > Critical Pressure, 
                                   # Elastic Deformation and Rp = ro
            Rp.append(ro)
            
        else:
            Rp.append(radius_plastic_zone(ro, Po, Pi, k, uni_comp_str))
            displ_plast.append(inward_radial_disp_plastic(ro,Po,Pcr,v,E,Rp[i-1],Pi))
        Pi -= 0.5
    #print(Ui)
    #print(Rp)
    #print(CharCurve)
    #plt.plot(Rp, PiList)        #Works for plotting 
    #plt.plot(CharCurve, PiList)
    plt.plot(displ_plast)
    plt.show()



if __name__ == "__main__":
    main()
