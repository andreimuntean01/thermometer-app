class Thermometer:
	def __init__ (self, temp):
		self.temp = temp


	def get_temp(self, unit = "C"):
		if unit == "C":
			return self.temp
		elif unit == "F":
			return self.to_fahrenheit(self.temp)
	def set_temp(self, temp):
		self.temp = temp

	def to_celsius(self,temp):
		temp = (temp - 32) * 5 / 9
		return temp
	def to_fahrenheit(self, temp):
		temp = temp * 9 / 5 +32
		return temp