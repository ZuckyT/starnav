import sys
sys.path.insert(0, "/home/brynm/sf2022/testPrograms/")

from convertCoord import *

import time
import math
from astroplan import FixedTarget
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import transforms
#Days Since J2000
divisor = float(4)
timer = float(time.time())
timers = time.gmtime(timer)
print("Timers GmTime: ", timers)
timers= time.strptime("4/1/2022 02:35", "%d/%m/%Y %H:%M")
print("Timers: ", timers)
years = timers.tm_year - 2000
iyears = int(years)
totalDays=years*365 #Years
totalDays=(timers.tm_min/60)+totalDays #Minutes
totalDays=(timers.tm_hour/24)+totalDays #Hours
totalDays=totalDays+timers.tm_yday #Days
for x in range (iyears): #Leap Years
	if (x%4) == 0:
		totalDays = totalDays + 1
totalDays=totalDays-1.5 #Cause January 1st 2000
print(totalDays)


#LST
def findLST(longitude):
	utcDecimal = (timers.tm_min/60)+(timers.tm_hour)
	lst = 100.46 + (.985647*totalDays) + longitude + (15*utcDecimal)
	while lst>360:
    		lst=lst-360
	return lst

#Hour Angle
def hourAngler(name, lst):
	star = FixedTarget.from_name(name)
	hourAngle = lst-(star.ra.degree)
	if(hourAngle<0):
		hourAngle=hourAngle+360
	return hourAngle, star

def sin(number):
	number = math.radians(number)
	number = math.sin(number)
	return number

def cos(number):
	number = math.radians(number)
	number = math.cos(number)
	return number

def sinD(number):
	number = np.sin(np.radians(number))
	return number

def cosD(number):
        number = np.cos(np.radians(number))
        return number

def convert(p, phi, theta):
	phi = 90-phi
	x = p*(sinD(phi))*(cosD(theta))
	y = p*(sinD(phi))*(sinD(theta))
	z = p*(cosD(phi))
	#print("X: ", x, " Y: ", y, " Z: ", z)
	return x, y, z
#Altitude Calculation
stars=["Altair", "Atlas", "Polaris", "Aldebaran", "Menkar", "Deneb", "Spica", "Vega", "Arcturus", "Canopus", "Betelgeuse", "Algol", "Sirius", "Hadar", "Fomalhaut", "Pollux", "Avior", "Procyon", "Rigel", "Hadar", "Acrux"]
def altAz(name):
	global hourAngle
	altitude = azimuth = 0.0
	latitude = 41.47015
	longitude = -81.30850
	lst = findLST(longitude)
	hourAngle, star = hourAngler(name, lst)
	#Switch All to Degrees for Trig Calculation
	altitudeS = (sin(star.dec.degree)*sin(latitude))+(cos(star.dec.degree)*cos(latitude)*cos(hourAngle))
	altitudeS = round(altitudeS, 4)
	while(round(math.sin(math.radians(altitude)), 4)!=altitudeS):
		altitude=altitude+.0001
		if(altitude>=90):
			return -1, -1
	azimuthS = (sin(star.dec.degree)-(sin(altitude)*sin(latitude))) / (cos(altitude)*cos(latitude))
	azimuthS = round(azimuthS, 4)
	while(round(math.cos(math.radians(azimuth)), 4)!=azimuthS):
		azimuth=azimuth+.0001
	if sin(hourAngle)>=0:
		azimuth=360-azimuth
	print("Azimuth: ", azimuth)
	print("Altitude: ", altitude)
	return azimuth, altitude
	print()
plot1 = plt.figure(1)
ax = plt.subplot(111, projection = 'polar')
xArr = [0]
yArr = [0]
k = 0
for x in stars:
	print("Doing Star ", x)
	(azimuth, altitude) = altAz(x)
	if(altitude==-1):
		print("Not Viewable")
		continue
	ax.plot(math.radians(azimuth), 90-altitude, 'w.')
	ax.annotate(x, (math.radians(azimuth), 90-altitude), color='white')
	(xPos, yPos, zPos) = convert(90, altitude, azimuth)
	xArr.append(xPos)
	yArr.append(-yPos)
	k=k+1
ax.set_facecolor('#000000')
ax.set_rmax(90)
ax.set_theta_zero_location("N")
plot2 = plt.figure(2)
plt.scatter(yArr, xArr)
plt.axis([-90, 90, -90, 90])
plt.grid()
plt.show()
