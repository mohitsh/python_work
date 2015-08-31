

class Vertex:
	def __init__(self,key):
		self.id = key
		self.connectedTo = {}
		self.color = 'white'
		self.dist = sys.maximize
		self.pred = None
		self.disc = 0
		self.fin = 0

	def addNeighbour(self,nbr,weight = 0):
		self.connectedTo[nbr] = weight
		
	def setColor(self,color):
		self.color = color
		
	def setDistance(self,d):
		self.dist = d

	def setPred(self,p):
		self.pred = p
	
	def setDiscovery(self,dtime):
		self.disc = dtime

	def setFinish(self,ftime):
		self.fin = ftime

	def getColor(self):
		return self.color

	def getDistance(self):
		return self.dist

	def getPred(self):
		return self.pred

	def getDiscovery(self):
		return self.disc

	def getFinish(self):
		return self.fin

	def getConnections(self):
		return self.connectedTo.keys()
	
	def __str__(self):
		return str(self.id) + ' connected to ' + str([x.id for x in self.connectedTo])

	def getId(self):
		return self.id
		
	def getWeight(self,nbr):
		return self.connectedTo[nbr]

class Graph:
	def __init__(self):
		self.vertList = {}
		self.numVertices = 0

	def addVertex(self,key):
		newVertex = Vertex(key)
		self.vertList[key] = newVertex
		self.numVertices  = self.numVertices + 1
		return newVertex

	def getVertex(self,n):
		if n in vertList:
			return vertList[n]
		else:
			return None

	def __contains__(self,n):
		return n in vertList[n]

	def addEdge(self,f,t,cost = 0):
		self.vertList[f].addneighbour(self.vertList[t],cost)

	def getVertices(self):
		return self.vertList.keys()

	def __iter__(self):
		return iter(self.vertList.values())

	


