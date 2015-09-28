
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

#s = Stack()
def findMax(h):
	s = Stack()
	area = []
	maxarea = 0
	for i in range(len(h)):
		# top of stack is less than value to be entered
		if len(s) == 0 or h[s.top()] <= h[i]:
		# push value to stack
			s.push(i)
		# if value to be entered is less than top of stack
		# pop the stack until we find a value less than the value to be entered
		else:
			# keep popping stack until a lesser value comes up
			while len(s) != 0 and h[s.top()] > h[i]:
				top = s.pop()
				if len(s) == 0:
					
					area = (h[top]*i)
					if area > maxarea:
						maxarea = area
				else:
					area = (h[top]*(i-s.top()-1))
					if area > maxarea:
						maxarea = area
			s.push(i)

	# at this point we have a maximum value and a stack
	# stack comprises of all the increasing element
	# and max value corresponds to popped elements and are in decreasig order or 
	# anamoly (largest)
	start = s.top()
	while len(s)!=0:
		#start = s.top()
		if len(s) == 1:
			area = h[s.pop()]*len(h)
			if area > maxarea:
				maxarea = area
		else:
			top = s.pop()
			area = h[top]*(start - s.top())
			if area >= maxarea:
				maxarea = area
	print maxarea
findMax(h)

