#Determines the probability that Kepler is able to detect a planet's transit given
#planet and star charactaristics

import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import csv 
import random
import math
from scipy.integrate import quad 

temp = pd.read_csv('KeplerFinal.txt') #insert real path
temp = temp.dropna().sort_values(by=['Teff']) #Table sorted by Teff least to greatest
data = list(temp['Teff']) 

def Radius(temp):
    return (temp*1.8395*10**5)-3.6169*10**8
def roi(temp):
    return (0.62817*temp**3)-(1235.15*temp**2)
#Outer orbital radius
def roo(temp):
    return (1.52*temp**3)-(2988.75*temp**2)

def detectionProb(rad,ri,ro):
    return (rad*np.log(ro/ri))/(ro-ri)

count=0
Sum=0
for value in data:
    probability=detectionProb(Radius(value),roi(value),roo(value))
    Sum=Sum+probability
    count=count+1
GeometricE=Sum/191451



