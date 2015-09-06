
class Empty(Exception):
	pass

class ArrayStack:
	
	def __init__(self):
		self._data = []
	
	def __len__(self):
		return len(self._data)

	def is_empty(self):
		return len(self._data) == 0

	def push(self,e):
		self._data.append(e)
		
	def top(self):
		if self.is_empty():
			raise Empty('Stack is empty')
		return self._data[-1]

	def pop(self):
		if self.is_empty():
			raise Empty('Stack is empty')
		return self._data.pop()
a = 'mohit'
stack = ArrayStack()
for ch in a:
	stack.push(ch)
ans = []
while not stack.is_empty():
	ans.append(stack.pop())

#print ''.join(ans)


def reverse(filename):
	s = ArrayStack()
	original = open(filename)
	for line in original:
		s.push(line.strip('\n'))
	original.close()

	output = open(filename, 'w')
	while not s.is_empty():
		output.write(s.pop() + '\n')
	output.close()
reverse('sample1.txt')	


''' stack check 

stack = ArrayStack()
print len(stack)
print stack.is_empty()
stack.push('jain')
print stack.is_empty()
print stack.pop()
print stack.is_empty()

  stack check ends '''
