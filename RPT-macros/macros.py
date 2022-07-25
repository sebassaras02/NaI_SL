# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 08:31:03 2021

@author: sebit
"""
# generacion de varios archivos txt
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys
import io 
# carga de datos
x_des= np.loadtxt('Posicionesmm.txt')
fin=x_des[len(x_des)-1]/2
for i in range(len(x_des)):
    x_des[i]=x_des[i]-fin
y=0
z=0

xd=np.array([25, 49, 73])
yd=np.array([0, -25, 25])
zd=np.array([20, 40, 60])

for i in range(len(x_des)):
    nombre ="pos"+ str(i+1) + ".mac" 
    archivo=open('C:/Universidad/PUBLICACIONES/# 1 RPT- NaI detector/Git-Repo/macros_25/'+ nombre,'w') # add your own path
    archivo.write("/gps/particle gamma \n") 
    archivo.write("/gps/energy 662 keV \n") 
    archivo.write("/gps/ene/type Gauss \n") 
    #archivo.write("/gps/pos/type Point \n")
    archivo.write("/gps/ang/type iso \n")
    archivo.write("/gps/pos/centre "+ str(x_des[i])+" " + str(y) +" " +str(z) + " m")
    archivo.write("\n")
    archivo.write("/NaI/detector/dimensions -24 25 20 cm \n")
    archivo.write("/run/reinitializeGeometry \n")
    archivo.write("/run/beamOn 1000000 \n") 
    archivo.close()
  

