''' Abstraction for Logic Gate
Gates are primarily devided into two categories
Binary and Unary
Further devisions include And, Or, Not gates.
A Connector class is provided to connect the nodes and
make a complete circuit. 
'''

class LogicGate:
	def __init__(self,n):
		self.label = n
		self.output = None

	def getLabel(self):
		return self.label
	
	def getOutput(self):
		self.output = self.performGateLogic()
		return self.output


class BinaryGate(LogicGate):
	def __init__(self,n):
		LogicGate.__init__(self,n)
		
		self.pinA = None
		self.pinB = None

	def getPinA(self):
		if self.pinA == None:
			self.pinA = int(input('enter pinA for gate %s --> ' %(self.getLabel())))
			return self.pinA
		else:
			return self.pinA.getFrom().getOutput()

	def getPinB(self):
		if self.pinB == None:
			self.pinB = int(input('enter pinB for gate %s --> ' %(self.getLabel())))
			return self.pinB
		else:
			return self.pinB.getFrom().getOutput()	
	
	def setNextPin(self,source):
		if self.pinA == None:
			self.pinA = source
		else:
			if self.pinB == None:
				self.pinB = source
			else:
				raise RuntimeError("No Empty pins found")
		
		
class UnaryGate(LogicGate):
	def __init__(self,n):
		LogicGate.__init__(self,n)

		self.pin = None

	def getPin(self):
		if self.pin == None:
			self.pin = int(input('enter pin for gate %s --> ' %(self.getLabel())))
			return self.pin
		else:
			return self.pin.getFrom().getOutput()
	def setNextPin(self,source):
		if self.pin == None:
			self.pin = source
		else:
			raise RuntimeError("No empty pins found")
		

class AndGate(BinaryGate):
	def __init__(self,n):
		BinaryGate.__init__(self,n)

	def performGateLogic(self):
		
		a = self.getPinA()
		b = self.getPinB()
		if a == 1 and b == 1:
			return 1
		else: 
			return 0

class OrGate(BinaryGate):
	def __init__(self,n):
		BinaryGate.__init__(self,n)

	def performGateLogic(self):
		a = self.getPinA()
		b = self.getPinB()
		
		if a == 0 and b == 0:
			return 0 
		else: 
			return 1

class NotGate(UnaryGate):
	def __init__(self,n):
		UnaryGate.__init__(self,n)
	
	def performGateLogic(self):
		a = self.getPin()
		if a == 1:
			return 0 
		else:
			return 1

class Connector:
	
	def __init__(self,fgate,tgate):
		self.fromgate  = fgate
		self.togate = tgate
	
		tgate.setNextPin(self)

	def getFrom(self):
		return self.fromgate

	def getTo(self):
		return self.togate


	def getPin(self):
		if self.pinA == None:
			self.pinA = int(input('enter pinA for gate %s --> ' %(get.label())))



def main():
	g1 = AndGate("G1")
	g2 = AndGate("G2")
	g3 = OrGate("G3")
	g4 = NotGate("G4")	
	c1 = Connector(g1,g3)
	c2 = Connector(g2,g3)
	c3 = Connector(g3,g4)
	print g4.getOutput()

main()
