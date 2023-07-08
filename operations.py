import math

class operations:
	def sin(number):
        	number = math.radians(number)
        	number = math.sin(number)
        	return number

	def cos(number):
	        number = math.radians(number)
	        number = math.cos(number)
	        return number

	def asin(number):
	        number = math.radians(number)
	        number = math.degrees(math.asin(number))
	        return number

	def acos(number):
	        number = math.radians(number)
		print(math.acos(number))
	        number = math.degrees(math.acos(number))
	        return number
