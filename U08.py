#!/usr/bin/python
# encoding=utf-8

"""Übung 08 Numerisches Ableiten"""
#Markus Klemm WS12/13 Phy-BA

import matplotlib.pyplot as plt
import numpy as np

FILENAME = "Bewegung.dat"

f = np.loadtxt(FILENAME)
m = 7.257 #Masse des Körpers kg
g = 9.81 #m/s

def ZDiff(x,y):
    """Übernimmt die Arrays x und y übergibt ein Array mit den Ableitungen"""
    
    xplus1 = x[2:]
    xminus1 = x[:-2]
    yplus1 = y[2:]
    yminus1 = y[:-2]
    
    return (yplus1 - yminus1) / (xplus1 - xminus1)
   
vx = ZDiff(f[:,0],f[:,1])
vz = ZDiff(f[:,0],f[:,2])



plt.show()

#Ekin = 0.5*m*(vx**2 + vz**2)
#Epot = m*g*f[:,2]



    