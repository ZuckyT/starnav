import time
import math
from astroplan import FixedTarget
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
	print(utcDecimal)
	lst = 100.46 + (.985647*totalDays) + longitude + (15*utcDecimal)
	while lst>360:
    		lst=lst-360
	return lst

#Hour Angle
def hourAngle(name, lst):
	star = FixedTarget.from_name(name)
	hourAngle = lst-(star.ra.degree)
	if(hourAngle<0):
		hourAngle=hourAngle+360
	return hourAngle, star

#Altitude Calculation
for x in range (-180, 180, 20):
	name = input("Name of Star: ")
	lst = findLST(x)
	hourAngle, star = hourAngle(name, lst)
	print("Star Type: ", star)
	altitudeS = (math.sin(star.dec.degree)*math.sin(x))+(math.cos(star.dec.degree)*math.cos(x)*math.cos(hourAngle))
	altitudeS = round(altitudeS, 5)
	print("Altitudes: ", altitudeS)
	y=0.0
	while(round(math.sin(math.radians(y)), 5)!=altitudeS):	
		y=y+.00001
	print("Finished, Altitude is: ", y)
	print(y)
	altitude = math.asin(altitudeS)
	print("Latitude: " + str(x))
	azimuth = (math.cos(star.dec.degree)-(math.sin(altitude)*math.sin(x))/(math.cos(altitude)*math.cos(x)))
	azimuth = math.acos(azimuth)
	print("Altitude: ", altitude)
	print("Azimuth: ", azimuth)
