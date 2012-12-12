#!/usr/bin/python
# encoding=utf-8

"""Übung 08 Numerisches Ableiten"""
#Markus Klemm WS12/13 Phy-BA


import numpy as np

FILENAME = "Bewegung.dat"

f = np.loadtxt(FILENAME)

#print f[:,0]
def ZDiff(x,y):
    """Übernimmt die Arrays x und y übergibt ein Array mit den Ableitungen"""
    
    xplus1 = x[1:]
    xminus1 = x[:-1]
    yplus1 = y[1:]
    yminus1 = y[:-1]
    
    return (yplus1 - yminus1) / (xplus1 - xminus1)
   
print ZDiff(f[:,0],f[:,1])

    