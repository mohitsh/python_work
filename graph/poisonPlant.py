
class Stack:
	def __init__(self):
		self._data = []
	def __len__(self):
		return len(self._data)
	def is_empty(self):
		return len(self._data) == 0
	def top(self):
		return self._data[-1]
	def pop(self):
		return self._data.pop()
	def __str__(self):
		return str(self._data)
	def push(self,item):
		self._data.append(item)


n = int(raw_input())
arr1 = raw_input().split()
arr = [int(x) for x in arr1]

#print n
#print arr

def poison(n,arr):
	s = []
	mark = []
	for i in range(n):
		if len(s) == 0 or arr[i] <= s[-1]:
			#print "i >",i,"s >",s
			s.append(arr[i])
			mark.append(1)
		else:
			#print "i >",i,"s >",s
			s.append(arr[i])
			mark.append(0)
	#print s

	s1 = []
	for i in range(len(mark)):
		if mark[i] == 1:
			s1.append(s[i])

	return s1
	


done = False
#arr  = poison(len(arr),arr)
start = n
count = 0
while not done:
	dude = poison(start,arr)
	#print dude
	if len(dude) != start:
		arr = dude
		start = len(arr)	
		count = count + 1
	
	else:
		done = True
print count
