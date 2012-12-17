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

Ekin = np.array(0.5*m*(vx**2 + vz**2))
Epot = np.array(m*g*f[:,2])

Eking = np.array(0.5*m*(vxg**2 + vzg**2))
Epotg = np.array(m*g*f[:,2])

Eges = np.array(Epot[1:-1] + Ekin)
Egesg = np.array(Epotg + Eking)

plt.figure()
plt.title("Energien")
plt.ylabel("Energie in Joule")
plt.xlabel("Zeit in Sekunden")

plt.plot(Ekin,label="Kinetische Energie")
plt.plot(Epot,label="Potentielle Energie")
plt.plot(Eges,label="Gesamtenergie")

plt.legend()

plt.figure()
plt.title("Energien per Gradient")
plt.ylabel("Energie in Joule")
plt.xlabel("Zeit in Sekunden")

plt.plot(Eking,label="Kinetische Energie")
plt.plot(Epotg,label="Potentielle Energie")
plt.plot(Egesg,label="Gesamtenergie")

plt.legend()

plt.show()





    