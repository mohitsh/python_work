
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
			raise Error("stack is empty")
		return self._data[-1]
	def pop(self):
		if self.is_empty():
			raise Error("stack is empty")
		return self._data.pop()
	def __str__(self):
		return str(self._data)

n = int(raw_input())
h1 = raw_input().split()
h = [int(x) for x in h1]
#print h

s = Stack()
arr = []
popped = 0
for i in range(len(h)):
	if len(s) == 0 or h[i] > s.top()[0]:
		s.push([h[i],i,0])
	elif h[i] < s.top()[0]:
		while len(s) != 0 and h[i] < s.top()[0]:
			top = s.pop()
			popped = popped + 1
			if len(s) == 0:
				arr.append(top[0]*(i-top[1]+top[2]))
			else:
				arr.append(top[0]*(i-top[1]))

		s.push([h[i],i,popped])

#print "array", arr
#ans = []
#while len(s) != 0:
#	ans.append(s.pop())

#print "stack", s
#print "array", arr
dude = []
while len(s) != 0:
	dude.append(s.pop())
#print "dude", dude

for i in range(len(dude)):
	start = dude[0][1]
	if len(dude) == 1:
		arr.append(dude[0][0])
	else:
		if i == 0:
			arr.append(dude[i][0]*(start- dude[i+1][1]))
		elif i == len(dude)-1:
			arr.append(dude[i][0]*(start+1))
		else:
			arr.append(dude[i][0]*(start-dude[i+1][1]))
print max(arr)

