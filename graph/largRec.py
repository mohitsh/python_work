
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

arr = [h[0]]
for i in range(len(h)-1,-1,-1):
	s.push(h[i])

#print s
dude = len(s)
for i in range(len(s)):	
	top = s.pop()
	if top > s.top():
		arr.append(s.top()*(dude-len(s)))
	else:
		arr.append(top*(dude-len(s)))


print s
print arr
	
