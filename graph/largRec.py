
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
print h

s = Stack()
arr = []

for i in range(len(h)):
	if len(s) == 0 or h[i] > h[s.top()]:
		s.push(i)
	elif h[i] < h[s.top()]:
		while h[i] < h[s.top()] and len(s) != 0:
			top = s.pop()
			if len(s) > 0:
				arr.append(h[top]*(top-s.top()))
			elif len(s) == 0:
				arr.append(h[top]*(top))
		s.push(i)


ans = []
while len(s) != 0:
	ans.append(s.pop())

print "ans", ans

for i in range(len(ans)):
	if i == 0:
		arr.append(h[ans[i]]*(ans[i] - ans[i+1]))
	elif i == len(ans) - 1:
		arr.append(h[ans[i]]*len(h))
	else:
		arr.append(h[ans[i]]*(ans[i-1]-ans[i+1]))
'''
while len(s) > 1:	
	top = s.pop()
	arr.append(h[top]*(top-s.top()))
if len(s) == 1:
	top = s.pop()
	arr.append(h[top]*(len(arr)))

'''
print arr

