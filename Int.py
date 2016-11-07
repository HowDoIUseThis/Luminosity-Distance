"""
This is intro program used to show that I can do computer stuff


Christopher Stewart 11/04/16
"""
import math
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


def simpleInt(type,lowerBound,upperbound,accuracy):
    tempSpace = linespace(lowerBound,upperbound,accuracy)
    sum = 0
    for x in tempSpace:
        sum += eCalc(type,x,Omega_M,Omega_K,Omega_L)
    return sum*(upperbound-lowerBound)/accuracy



"""
For testing results
"""
z0=simpleInt(1,0,0.5,500)
z1=simpleInt(1,0,1,500)
z6=simpleInt(1,0,6,500)
print("The comoving distances are:","\nZ = 0.5: ",z0, "\nZ = 1: ",z1, "\nZ = 6: ",z6)
lz0=(1.5*z0)
lz1=(2*z1)
lz6=(7*z6)
print("When OmegaK is 0 the Luminosity distances are:","\nZ = 0.5: ",lz0, "\nZ = 1: ",lz1, "\nZ = 6: ",lz6)
lb0 = simpleInt(0,0,0.5,500)
lb1 = simpleInt(0,0,1,500)
lb6 = simpleInt(0,0,6,500)
print("The lookback timess are:","\nZ = 0.5: ",lb0, "\nZ = 1: ",lb1, "\nZ = 6: ",lb6)