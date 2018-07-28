class Calculator():

	def __init__(self,name):
	     print ("constructor called")
	     self.name = name
	

	def  add(self,a,b):
	     result = a+b
	     return result
	
	
	def  sub(self,a,b):
	     return (a-b)
	
	def  sub(self,a,b):
	     return (a*b)

	def  sub(self,a,b):
	     return (a/b)
	
obj1 = Calculator("what name")
result = obj1.add(3,4)
print(result)
	
	
