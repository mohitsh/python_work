
class Graph:

        def __init__(self,graph_dict = {}):
                self._graph_dict = graph_dict

        def add_vertex(self,vertex):
                if vertex not in self._graph_dict:
                        self._graph_dict[vertex] = []

        def add_edge(self,edge):
                (vertex1,vertex2) = edge
                if vertex1 in self._graph_dict:
                        self._graph_dict[vertex1].append(vertex2)
                else:
                        self._graph_dict[vertex1] = [vertex2]
			
        def vertices(self):
                return list(self._graph_dict.keys())

        def edges(self):
                return self.generate_edges()

        def generate_edges(self):
                edges = []
                for vertex in self._graph_dict:
                        for neighbor in self._graph_dict[vertex]:
                                if [vertex,neighbor] not in edges:
                                        edges.append([vertex,neighbor])
                                        edges.append([neighbor[0],[vertex,neighbor[1]]])
                return edges

        def incident_edges(self,u):
                dude = []
                for k in self.generate_edges():
                        if k[0] == u:
                                dude.append(k)

                return dude

        def __str__(self):
                res = "vertices: "
                for k in self._graph_dict.keys():
                        res += str(k) + " "
                res += "\nedges: "
                for k in self.generate_edges():
                        res += str(k) + " "

                return res

        def get_edge(self,u,v):
                for e in self.incident_edges(u):
                        if e[1] == v:
                                return e
	def out_degree(self,u):
		count = 0
		for e in self.generate_edges():
			if e[0] == u:
				count += 1
		return count
	
	def in_degree(self,u):
		count = 0
		for e in self.generate_edges():
			if e[1][0] == u:
				count += 1
		return count

			
"""
g = Graph()
g.add_vertex('v1')
g.add_vertex('v2')
g.add_vertex('v3')
g.add_vertex('v4')
g.add_vertex('v5')
g.add_vertex('v6')
g.add_vertex('v7')

g.add_edge(['v1',['v4',1]])
g.add_edge(['v1',['v5',1]])
g.add_edge(['v1',['v7',1]])
g.add_edge(['v4',['v5',1]])
g.add_edge(['v3',['v4',1]])
g.add_edge(['v3',['v5',1]])
g.add_edge(['v2',['v3',1]])
g.add_edge(['v2',['v5',1]])
g.add_edge(['v2',['v6',1]])
g.add_edge(['v6',['v7',1]])
g.add_edge(['v5',['v6',1]])
g.add_edge(['v5',['v7',1]])
"""
"""

def topological_sort(g):
	topo = []
	ready = []
	incount = {}
	
	for u in g.vertices():
		incount[u] = g.in_degree(u)
		if incount[u] == 0:
			ready.append(u)
	while len(ready) > 0:
		u = ready.pop()
		topo.append(u)
		for e in g.incident_edges(u):
			v = e[1][0]
			incount[v] -= 1
			if incount[v] == 0:
				ready.append(v)
	return topo


g1 = Graph()
g1.add_vertex(1)
g1.add_vertex(2)
g1.add_vertex(3)
g1.add_vertex(4)

g1.add_edge([1,[2,5]])
g1.add_edge([1,[4,24]])
g1.add_edge([2,[4,6]])
g1.add_edge([3,[4,4]])
g1.add_edge([3,[2,7]])
"""
#print topological_sort(g1)

class prior_queue:
	def __init__(self):
		self.items = []
	def is_empty(self):
		return len(self.items) == 0
	def insert(self,item):
		self.items.append(item)
		return item
	def remove(self):
		maxi = 0
		for i in range(1,len(self.items)):
			if self.items[i][0] < self.items[maxi][0]:
				maxi = i
		item = self.items[maxi]
		del self.items[maxi]
		return item
	def update(self,loc,item):
		for i in self.items:
			if i == loc:
				i[0] = item[0]
				i[1] = item[1]
"""
q = prior_queue()
q.insert([11,'a'])
q.insert([8,'b'])
q.insert([6,'c'])
q.insert([100,'d'])
q.update([100,'d'],[10,'e'])

print q.remove()
print q.remove()
print q.remove()
print q.remove()
"""
def shortest_path_length(g,src):

	d = {}
	cloud = {}
	pq = prior_queue()
	pqlocator = {}
	
	for v in g.vertices():
		if v is src:
			d[v] = 0
		else:
			d[v] = float('inf')
		pqlocator[v] = pq.insert([d[v],v])
	
	while not pq.is_empty():
		key,u = pq.remove()
		#print key,u
		
		cloud[u] = key
		del pqlocator[u]
		for e in g.incident_edges(u):
			v = e[1][0]
			if v not in cloud:
				wgt = e[1][1]
				if d[u] + wgt < d[v]:
					d[v] = d[u] + wgt
					pq.update(pqlocator[v],[d[v],v])
	return cloud
		
"""
print shortest_path_length(g1,1)
print shortest_path_length(g1,3)
"""

g = Graph()


n_e = raw_input().split()
n,e = [int(x) for x in n_e]
for i in range(e):
        inp = raw_input().split()
        v1,v2,e = [int(x) for x in inp]
        g.add_vertex(v1)
        g.add_vertex(v2)
        g.add_edge([v1,[v2,e]])

start = int(raw_input())
path = shortest_path_length(g,start)
arr = []
for key in path:
	if key != start:
		print path[key],


"""
q = int(raw_input())
for i in range(q):
        inp = raw_input().split()
        v1,v2 = [int(x) for x in inp]
        ans = shortest_path_length(g,v1)
	if ans[v2] == float('inf'):
		print -1
	else:
		print ans[v2]
	
"""


