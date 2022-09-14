#Divides all the stars in the dataset into gernalized bins
#The bins needed to be at least 100 Teff wide and have at least 100 data points

import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

temp = pd.read_csv('KeplerFinal.txt') #insert real path
temp = temp.dropna().sort_values(by=['Teff']) #Table sorted by Teff least to greatest
data = list(temp['Teff']) 

binTempArr = [data[0]]

def histo(minTempDifference,minNumIndicies):
	lastTemp = 0
	numIndicies = 0
	for i in range(0,len(data)): #makes sure each bin is at least 100 Teff wide, and each bin has at least 100 points
		numIndicies += 1
		if data[i] - lastTemp >= minTempDifference and numIndicies >= minNumIndicies:
			lastTemp = data[i]
			binTempArr.append(lastTemp)
			numIndicies = 0

	plt.hist(data, edgecolor='white', bins=binTempArr) #plots histogram with custom bins
	plt.xlabel("Temperature of Star (K)")
	plt.ylabel("Frequency")
	plt.title("Temperatures of Stars from the Kepler Dataset")
	plt.show() 

histo(100,100)
temp1 = temp.to_numpy() #finds all the kepID's of stars in each bin
temp2 = temp1[:,1]
ids = temp1[:,0]
test2 = np.where((temp2> 3109) & (temp2< 3177)) #bin 1, need to write loop to do for all bins and put in array
ids[test2]
