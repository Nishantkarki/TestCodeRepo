import os
import random
import sys

class Math:

	# _a = 0
	# _b = 0

	def __init__(self, a, b):
		self._a =a
		self._b = b		


	#getter 
	def getA(self):
		return self._a;
	#getter 
	def getB(self):
		return self._b;
	
	#setter
	def setValue(a,b):
		self._a = a
		self._b = b


	def multiply(self):
		return (getA()*getB())

	def subtract(self):
		return (self.getA()-self.getB())

	def addCalc(self):
		return (self.getA()+self.getB())

	def test():
		print("I am class method")
		
		


obj1 = Math(20,40)
retVal = obj1.addCalc()

print("Calling class method")
Math.test()

print(retVal)





