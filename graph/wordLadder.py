
from graph2 import Graph, Vertex

def  buildGraph(wordFile):
	d = {}
	g = Graph()
	wfile = open(wordFile,'r')
	
	for line in wfile:
		word = line[:-1]
		#print word
		for i in range(len(word)):
			bucket = word[:i] + '_' + word[i+1:]
			if  bucket in d:
				d[bucket].append(word)
			else:
				d[bucket] = [word]
	for key in d:
		print key, d[key]
	print d.keys()
	print d.values()
	for bucket in d.keys():
		for word1 in d[bucket]:
			for word2 in d[bucket]:
				if word1 != word2:
					g.addEdge(word1,word2)
	return g                                        





buildGraph('words.txt')
