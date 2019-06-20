class testing:

	clsvar = "I am Class variable"
	def __init__(self, name, age):
		self.name = name
		self.age = age
		
	def address(self, address):
		self.address = address
		self.pin = 124578
		
o = testing("Aalam", 26)
print o.name, o.age
o.address("Saharanpur")
print o.address, o.pin, o.clsvar