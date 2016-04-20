import math
import matplotlib.pyplot as plt
import numpy as np

#The purpose of this program is to calculate the Radial, Tangential and Shear Stress in a circular tunnel given input parameters.

def RadialStress(Pz, Diameter, k, Theta, r, Pi):
    """
    RadialStress Function will Return the Radial Stress at a given point (r, Theta) and input parameters (Pz, Diameter, k, Pi)
    """
    a = Diameter/2
    Theta = math.radians(Theta)
    return (1/2)*Pz*((1+k)*(1-(a**2)/(r**2))+(1-k)*(1-4*(a**2)/(r**2)+3*(a**4)/(r**4))*math.cos(2*Theta))+Pi*((a**2)/(r**2))

def TangentialStress(Pz, Diameter, k, Theta, r, Pi):
    """
    TangentialStress Function will Return the Tangential Stress given point (r, Theta) and input parameters (Pz, Diameter, k, Pi)
    """
    a = Diameter/2
    Theta = math.radians(Theta)
    return (1/2)*Pz*((1+k)*(1+(a**2)/(r**2))-(1-k)*(1+3*(a**4)/(r**4))*math.cos(2*Theta))-Pi*((a**2)/(r**2))

def ShearStress(Pz, Diameter, k, Theta, r):
    """
    ShearStress Function will Return the Tangential Stress given point (r, Theta) and input parameters (Pz, Diameter, k, Pi)
    """
    a = Diameter/2
    Theta = math.radians(Theta)
    return (1/2)*Pz*(-(1-k)*(1+2*(a**2)/(r**2)-3*(a**4)/(r**4))*math.sin(2*Theta))

def OverStressZone(RadStress, TanStress, ShrStress, c=800, phi=32):
    #
    UCompStr = 2*c*math.cos(math.radians(phi))/(1-math.sin(math.radians(phi)))
    
    Sigma1 = (1/2)*(RadStress+TanStress)+(((1/4)*(RadStress-TanStress)**2+ShrStress^2))

    if Sigma1>UCompStr:
        return 1
    else: 
        return 0
    
def main():

    RadStress = []
    TanStress = []
    ShrStress = []
    r_list = []
    Pz = 2500 * 1.1
    Pi = 0
    Diameter = 10
    k = 0.5
    Theta = 90
    #Determine Stresses for K = 0.5 and Plot Resulting Stresses
    for r in range(5,60,1):
        RadStress.append(RadialStress(Pz, Diameter, k, Theta, r, Pi))
        TanStress.append(TangentialStress(Pz, Diameter, k, Theta, r, Pi))
        ShrStress.append(ShearStress(Pz, Diameter, k, Theta, r))        
        r_list.append(r)
    plt.figure(1)
    #plt.subplot(311)
    plt.plot(r_list, RadStress, '|-', label='Radial Stress, K= {}'.format(k))
    plt.plot(r_list, TanStress, label='Tangential Stress, K= {}'.format(k))
    plt.xlabel('Feet')
    plt.ylabel('Stress (PSI)')
    plt.title('Tangential and Radial Stresses'.format(k))

    #Determine Stresses for K = 1.0 and Plot Resulting Stresses
    k = 1
    RadStress = []
    TanStress = []
    ShrStress = []
    r_list = []
    for r in range(5,60,1):
        RadStress.append(RadialStress(Pz, Diameter, k, Theta, r, Pi))
        TanStress.append(TangentialStress(Pz, Diameter, k, Theta, r, Pi))
        ShrStress.append(ShearStress(Pz, Diameter, k, Theta, r))
        r_list.append(r)

    #plt.subplot(312)
    plt.plot(r_list, RadStress, '|-', label='Radial Stress, K= {}'.format(k))
    plt.plot(r_list, TanStress, label='Tangential Stress, K= {}'.format(k))
    plt.xlabel('Feet')
    plt.ylabel('Stress (PSI)')
    plt.title('Tangential and Radial Stresses, K = {}'.format(k))

    #Determine Stresses for K = 2.5 and Plot
    k = 2.5
    RadStress = []
    TanStress = []
    ShrStress = []
    r_list = []
    for r in range(5,60,1):
        RadStress.append(RadialStress(Pz, Diameter, k, Theta, r, Pi))
        TanStress.append(TangentialStress(Pz, Diameter, k, Theta, r, Pi))
        ShrStress.append(ShearStress(Pz, Diameter, k, Theta, r))
        r_list.append(r)

    #plt.subplot(313)
    plt.plot(r_list, RadStress, '|-', label='Radial Stress, K= {}'.format(k))
    plt.plot(r_list, TanStress, label='Tangential Stress, K= {}'.format(k))
    plt.xlabel('Feet')
    plt.ylabel('Stress (PSI)')
    plt.title('Tangential and Radial Stresses Circular Tunnel'.format(k))
    plt.legend()
#Graphing for Internal Pressures
    Pi = 500
    
    k = 0.5
    RadStress = []
    TanStress = []
    ShrStress = []
    r_list = []
    #Determine Stresses for K = 0.5 and Plot Resulting Stresses
    for r in range(5,60,1):
        RadStress.append(RadialStress(Pz, Diameter, k, Theta, r, Pi))
        TanStress.append(TangentialStress(Pz, Diameter, k, Theta, r, Pi))
        ShrStress.append(ShearStress(Pz, Diameter, k, Theta, r))
        r_list.append(r)
    plt.figure(2)
    #plt.subplot(311)
    plt.plot(r_list, RadStress)
    plt.plot(r_list, TanStress)
    plt.xlabel('Feet')
    plt.ylabel('Stress (PSI)')
    plt.title('Tangential and Radial Stresses, K = {}, Internal Pressure of 500'.format(k))

    #Determine Stresses for K = 1.0 and Plot Resulting Stresses
    k = 1
    RadStress = []
    TanStress = []
    ShrStress = []
    r_list = []
    for r in range(5,60,1):
        RadStress.append(RadialStress(Pz, Diameter, k, Theta, r, Pi))
        TanStress.append(TangentialStress(Pz, Diameter, k, Theta, r, Pi))
        ShrStress.append(ShearStress(Pz, Diameter, k, Theta, r))
        r_list.append(r)

    #plt.subplot(312)
    plt.plot(r_list, RadStress)
    plt.plot(r_list, TanStress)
    plt.xlabel('Feet')
    plt.ylabel('Stress (PSI)')
    plt.title('Tangential and Radial Stresses, K = {}, Internal Pressure of 500'.format(k))

    #Determine Stresses for K = 2.5 and Plot
    k = 2.5
    RadStress = []
    TanStress = []
    ShrStress = []
    r_list = []
    for r in range(5,60,1):
        RadStress.append(RadialStress(Pz, Diameter, k, Theta, r, Pi))
        TanStress.append(TangentialStress(Pz, Diameter, k, Theta, r, Pi))
        ShrStress.append(ShearStress(Pz, Diameter, k, Theta, r))
        r_list.append(r)

    #plt.subplot(313)
    plt.plot(r_list, RadStress)
    plt.plot(r_list, TanStress)
    plt.xlabel('Feet')
    plt.ylabel('Stress (PSI)')
    plt.title('Tangential and Radial Stresses, K = {}, Internal Pressure of 500'.format(k))    

    plt.show()

    #Problem 2

    RadStress2 = []
    TanStress2 = []
    ShrStress2 = []
    r_list2 = []
    Pz = 2500 * 1.1
    Pi = 0
    Diameter = 10
    k = 0.5
    Theta = 0
        #for r in range(5, 10, 1):
    
            #RadStress2.append(RadialStress(Pz, Diameter, k, Theta, r, Pi))
            #TanStress2.append(TangentialStress(Pz, Diameter, k, Theta, r, Pi))
            #ShrStress2.append(ShearStress(Pz, Diameter, k, Theta, r))
            #r_list2.append(r)

if __name__ == "__main__":
    main()
