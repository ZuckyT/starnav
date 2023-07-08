import time
import math
from astroplan import FixedTarget
import numpy as np
import matplotlib.pyplot as plt
#Days Since J2000
divisor = float(4)
timer = float(time.time())
timers = time.gmtime(timer)
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
	#print(utcDecimal)
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

#Altitude Calculation
stars=["Altair", "Deneb", "Spica", "Vega", "Arcturus", "Canopus", "Betelgeuse", "Algol", "Sirius", "Hadar", "Fomalhaut", "Pollux", "Avior"]
def altAz(name):
	global hourAngle
	latitude = 41.47015
	longitude = -81.30850
	#name = input("Name of Star: ")
	lst = findLST(longitude)
	hourAngle, star = hourAngler(name, lst)
	#print("RA: ", star.ra, " Dec: ", star.dec)
	#print(star)
	#Switch All to Degrees for Trig Calculations
	altitudeS = (sin(star.dec.degree)*sin(latitude))+(cos(star.dec.degree)*cos(latitude)*cos(hourAngle))
	altitudeS = round(altitudeS, 4)
	altitude=0.0	
	while(round(math.sin(math.radians(altitude)), 4)!=altitudeS):
		altitude=altitude+.0001
		if(altitude>=90):
			print("Got Here")
			return -1, -1
		#print(altitude)
	#print("Finished, Altitude is: ", altitude)
	azimuthS = sin(star.dec.degree)-(sin(altitude)*sin(latitude))
	azimuthS = (azimuthS) / (cos(altitude)*cos(latitude))
	azimuthS = round(azimuthS, 4)
	azimuth=0
	while(round(math.cos(math.radians(azimuth)), 4)!=azimuthS):
		azimuth=azimuth+.0001
		#if
	if sin(hourAngle)>=0:
		azimuth=360-azimuth
		print("Azimuth is being subtracted from 360")
	print("Azimuth: ", azimuth)
	print("Altitude: ", altitude)
	return azimuth, altitude
	print()

ax = plt.subplot(111, projection = 'polar')

for x in stars:
	print("Doing Star ", x)
	(azimuth, altitude) = altAz(x)
	if(altitude==-1):
		print("Not Viewable")
		continue
	ax.plot(math.radians(azimuth), 90-altitude, 'w.')
	ax.annotate(x, (math.radians(azimuth), 90-altitude), color='white')
ax.set_facecolor('#000000')
ax.set_rmax(90)
ax.set_theta_zero_location("N")
plt.show()
