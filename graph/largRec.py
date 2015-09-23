
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

s = Stack()

n = int(raw_input())
h1 = raw_input().split()
h = [int(x) for x in h1]

arr = []
for i in range(len(h)-1,-1,-1):
	s.push(h[i])
print "stack below"
print s

for k in range(len(s)):
	elem = s.pop()
	if len(arr) != 0:
		top = arr[-1]
		if elem < top:
			arr.append(elem*(len(arr)+1))
	elif len(arr) == 0:
		arr.append(elem)

print "array below"
print arr


	
