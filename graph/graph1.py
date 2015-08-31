

class vertex:
	def __init__(self,key):
		self.id = key
		self.connecedTo = {}

	def addNeighbour(self,nbr,weight=0):
		self.connectedTo[nbr] = weight

	def getConnections(self):
		return self.connectedTo.keys()

	def __str__(self):
		return str(self.id) + ' connected to ' + str([x.id for x in self.connectedTo])

	def getId(self):
		return self.id

	def getWeight(self,nbr):
		return self.connectedTo[nbr]

	
