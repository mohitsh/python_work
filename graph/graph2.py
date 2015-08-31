import os
import sys

class Vertex:
	def __init__(self,key):
		self.id = key
		self.connectedTo = {}
		self.color = 'white'
		self.dist =  sys.maxsize
		self.pred = None
		self.disc = 0
		self.fin = 0

	def addNeighbour(self,nbr,weight = 0):
		self.connectedTo[nbr] = weight

	def setColor(self,color):
		self.color = color
	
	def setDistance(self,dist):
		self.dist = dist
	
	def setPred(self,pred):		
		self.pred = pred

	def setDisc(self,disc):
		self.disc = disc

	def setFin(self,fin):
		self.fin = fin

	def getFin(self):
		return self.fin
	
	def getDisc(self):
		return self.disc

	def getPred(self):
		return self.pred

	def getDistance(self):
		return self.disc

	def getColor(self):
		return self.color

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
		self.numVertices = self.numVertices + 1
		newVertex = Vertex(key)
		self.vertList[key] = newVertex
		return newVertex

	def getVertex(self,n):
		if n in vertList:
			return self.vertList[n]
		else:
			return None

	def __contains__(self,n):
		return n in self.vertList

	def addEdge(self,f,t,cost=0):
		self.vertList[f].addNeighbour(self.vertList[t], cost)

	def getVertices(self):
		return self.vertList.keys()

	def __iter__(self):
		return iter(self.vertList.values())

	

g = Graph()
for i in range(6):
	g.addVertex(i)

g.vertList

g.addEdge(0,1,5)
g.addEdge(0,5,2)
g.addEdge(1,2,4)
g.addEdge(2,3,9)
g.addEdge(3,4,7)
g.addEdge(3,5,3)
g.addEdge(4,0,1)
g.addEdge(5,4,8)
g.addEdge(5,2,1)

for v in g:
	for w in v.getConnections():
		print  "(%s,%s)" %(v.getId(),w.getId())












