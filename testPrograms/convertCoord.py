import math 
class convertCoord:

	def __init__(self):
		self.x=0
		self.y=0
		self.z=0
		self.number=0

	def sinA(self, number):
		self.number = math.radians(self.number)
		self.number = math.sin(self.number)
		return self.number

	def cosA(self, number):
		self.number = math.radians(self.number)
		self.number = math.cos(self.number)
		return self.number

	def convert(p, phi, theta):
		phi = 90-phi
		print("Phi: ", phi)
		self.x = p*(self.sinA(phi))*(self.cosA(theta))
		self.y = p*(self.sinA(phi))*(self.sinA(theta))
		self.z = p*(self.cosA(phi))
		print("X: ", self.x, " Y: ", self.y, " Z: ", self.z)
		return self.x, self.y, self.z
