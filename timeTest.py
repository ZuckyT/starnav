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
	print("Hour Angle: ", hourAngle)
	return hourAngle, star

def sin(number):
	number = math.radians(number)
	number = math.sin(number)
	return number

def cos(number):
	number = math.radians(number)
	number = math.cos(number)
	return number

def asin(number):
	print("Number: ", number)
	number = math.radians(number)
	print("Number in Radians: ", number)
	print("Asin of Number: ", math.asin(number))
	number = math.degrees(math.asin(number))
	print("Asin to Degrees: ", number)
	return number

def acos(number):
        number = math.radians(number)
        number = math.degrees(math.acos(number))
        return number
#Altitude Calculation
stars=["Altair", "Deneb", "Arcturus", "Vega", "Capella"]

def altAz(star):
latitude = 41.47015
longitude = -81.30850
print("Sin of 35 is:", sin(35))
name = input("Name of Star: ")
lst = findLST(longitude)
hourAngle, star = hourAngle(name, lst)
print("RA: ", star.ra, " Dec: ", star.dec)
print(star)
#Switch All to Degrees for Trig Calculations
altitudeS = (sin(star.dec.degree)*sin(latitude))+(cos(star.dec.degree)*cos(latitude)*cos(hourAngle))
altitudeS = round(altitudeS, 5)
altitude=0.0
while(round(math.sin(math.radians(altitude)), 5)!=altitudeS):
	altitude=altitude+.00001
	#print(altitude)
print("Finished, Altitude is: ", altitude)
azimuthS = sin(star.dec.degree)-(sin(altitude)*sin(latitude))
azimuthS = (azimuthS) / (cos(altitude)*cos(latitude))
azimuthS = round(azimuthS, 5)
azimuth=0
while(round(math.cos(math.radians(azimuth)), 5)!=azimuthS):
	azimuth=azimuth+.00001
if math.sin(hourAngle)<=0:
	azimuth=360-azimuth
	print("Azimuth is being subtracted from 360")
print("Azimuth: ", azimuth)
print("Altitude: ", altitude)
