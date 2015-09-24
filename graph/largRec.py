
class Stack:
	def __init__(self):
		self._data  = []
	def __len__(self):
		return len(self._data)
	def is_empty(self):
		return len(self._data) == 0
	def push(self,e):
		self._data.append(e)
	def top(self):
		if self.is_empty():
			raise Empty("stack is empty")
		return self._data[-1]
	def pop(self):
		if self.is_empty():
			raise Empty("stack is empty")
		return self._data.pop()
	def __str__(self):
		return str(self._data)

n = int(raw_input())
h1 = raw_input().split()
h = [int(x) for x in h1]

#print h

ans = [-1]
for i in range(len(h)):
	s = Stack()
	#print "iteration ", i
	for k in range(i,-1,-1):
		#print k
		if h[k] >= h[i]:
			s.push(h[k]) 
		else:
			break
	for j in range(i+1,len(h)):
		#print j
		if h[j] >= h[i]:
			s.push(h[j])
		else:
			break
	if h[i]*len(s) > ans[-1]:
		ans.append(h[i]*(len(s)))
	
print ans[-1]
