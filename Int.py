"""
This is intro program used to show that I can do computer stuff


Christopher Stewart 11/04/16
"""
import scipy.integrate as integrate
import matplotlib.pyplot as plt
import math
import numpy as np
"""
Test values and constants. Below is a list of things to remember:

Comoving distance:
    d_C  =  Int(0,Current Z, E^(1/2)
        E = Sqrt(Omega_M(1+z)^3 + Omega_k(1+z)^2 +Omega_L)


Transverse comoving distance: **This is piecewise with respect to Omega_K**

Omega_K > 0:
           d_M = d_H/(Sqrt(Omega_K)) sinh(sqrt(Omega_K)d_C(z)/d_H)
Omega_K = 0
           d_M = d_C(z)
Omega_K < 0
           d_M = d_H/(Sqrt(Omega_K)) sin(sqrt(abs(Omega_K))d_C(z)/d_H)



"""
H0 = 70 #km/s/Mpc
Omega_M = 0.3   #(matter, including dark matter)
Omega_L = 0.7  # (dark energy)
Omega_K = 0    #(no curvature)
T_h = 9.8*10**9

"""
Input:  Start (int)
        End   (int)
        Num   (int)
Return: Arrary (floats)

Function that mimics matlabs linespace function. The function creates any number (num)
of evenly spaced points from a starting point (start) to and ending point(end).
"""
def linespace(start, end, num):
    if num < 2:
        return end
    diff = (float(end) - start) / (num - 1)
    return [diff * i + start for i in range(num)] #returns the array of points



def eCalc(type,z,O_m,O_k,O_L):
    z3 = (1+z)**3
    z2 = (1+z)**2
    z1 = (1+z)
    if type == 1:
        E = math.sqrt(O_m*z3 +O_k*z2 + O_L)
    else:
        E = z1*math.sqrt(O_m*z3 +O_k*z2 + O_L)
    return 1/E

"Ok so this is pretty awful, but this is why we use things smart people make, numpy!"
def simpleInt(type,lowerBound,upperBound,accuracy):
    tempSpace = linespace(lowerBound,upperBound,accuracy)
    sum = 0
    for x in tempSpace:
        sum += eCalc(type,x,Omega_M,Omega_K,Omega_L)
    return sum*(upperBound-lowerBound)/accuracy

def accurateInt(type,lowerBound,upperBound):
    result = integrate.quad(lambda x: eCalc(type,x,Omega_M,Omega_K,Omega_L), lowerBound, upperBound)
    return result
				
def printOldInt():
    z0=simpleInt(1,0,0.5,500)
    z1=simpleInt(1,0,1,500)
    z6=simpleInt(1,0,6,500)
    print("The comoving distances are:","\nZ = 0.5: ",z0, "\nZ = 1: ",z1, "\nZ = 6: ",z6)
    lz0=(1.5*z0)
    lz1=(2*z1)
    lz6=(7*z6)
    print("When OmegaK is 0 the Luminosity distances are:","\nZ = 0.5: ",
										lz0, "\nZ = 1: ",lz1, "\nZ = 6: ",lz6)
    lb0 = simpleInt(0,0,0.5,500)
    lb1 = simpleInt(0,0,1,500)
    lb6 = simpleInt(0,0,6,500)
    print("The lookback timess are:","\nZ = 0.5: ",lb0, "\nZ = 1: ",lb1, "\nZ = 6: ",lb6)
    
def printAccInt():
    print("The comoving distances are:", "\nZ = 0.5: ", accurateInt(1,0,0.5)[0], "\nZ = 1: ", 
        accurateInt(1, 0, 1)[0], "\nZ = 6: ", accurateInt(1, 0, 6)[0])
   
    print("When OmegaK is 0 the Luminosity distances are:","\nZ = 0.5: ",1.5*(accurateInt(1,0,0.5)[0]), 
				"\nZ = 1: ", 2*(accurateInt(1, 0, 1)[0]), "\nZ = 6: ",7*(accurateInt(1, 0, 6)[0]))
   
    print("The lookback timess are:","\nZ = 0.5: ",accurateInt(0,0,0.5)[0],
					"\nZ = 1: ",accurateInt(0, 0, 1)[0], "\nZ = 6: ",accurateInt(0, 0, 6)[0])
    
def convToScale(i):
	return i[0]


"""
For testing results
"""
printAccInt()
"                       Plot of Luminosity vs Redshift                  "
"---------------------------------------------------------------------------"
d1 = 1.5*accurateInt(1,0,0.5)[0]
d2 = 2*(accurateInt(1, 0, 1))[0]
d3 = 7*(accurateInt(1, 0, 6))[0]
y = np.array([d1,d2,d3])
x = np.array([0.5,1.,6.])
plt.axis([0,10,0,16])
plt.plot(x, y, 'ro')
plt.xlabel('Redshift (z)')
plt.ylabel('Luminosity Distance-Dl (Mpc)')
plt.title('Luminosity Distance vs Redshift')
plt.grid(True)
plt.savefig("LD_vs_Rs.png")
plt.show()
"                       Plot of Lookback Time vs Redshift                  "
"--------------------------------------------------------------------------"
d1 = accurateInt(0,0,0.5)[0]
d2 = accurateInt(0, 0, 1)[0]
d3 = accurateInt(0, 0, 6)[0]
y = np.array([d1,d2,d3])
x = np.array([0.5,1.,6.])
plt.axis([0,8,0,1])
plt.plot(x, y, 'ro')
plt.xlabel('Redshift (z)')
plt.ylabel('Lookback Time (Gyr)')
plt.title('Lookback Time vs Redshift')
plt.grid(True)
plt.savefig("LB_vs_Rs.png")
plt.show()
