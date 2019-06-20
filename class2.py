from datetime import date

class CSStudent: 
      
    # Class Variable 
    stream = 'cse'      
      
    # The init method or constructor 
    def __init__(self, roll): 
          
        # Instance Variable 
        self.roll = roll             
  
    # Adds an instance variable  
    def setAddress(self, address): 
        self.address = address 
      
    # Retrieves instance variable     
    def getAddress(self):     
        return self.address
		
	@classmethod	
	def dateofBirth(cls, year):
		return ( date.today().year - year )

    @staticmethod    
    def test(name):
        return name

    @staticmethod
    def isAdult(age):
        return age > 18
    @classmethod
    def name(cls, n):
        print(n)
# Driver Code 
a = CSStudent(101) 
a.setAddress("Noida, UP") 
print(a.getAddress()) 
print(a.address) 
print(a.isAdult(32))
print(CSStudent.test("AALAMGEER"))
CSStudent.name("Srijan")
print(CSStudent.dateofBirth(21))