
class ArrayQueue:
	
	default_capacity = 10
	def __init__(self):
		self._front = 0
		self._data = [None]*ArrayQueue.default_capacity
		self._size = 0

	def __len__(self):
		return self._size

	def is_empty(self):
		return self._size == 0

	def first(self):
		return self._data[self._front]

	def enqueue(self,e):
		if len(self._data) == self._size:
			self._resize(2*len(self._data))
		avail = (self._front + self._size)%len(self._data)
		self._data[avail] = e
		self._size += 1

	def dequeue(self):
		answer = self._data[self._front]
		self._data[self._front] = None
		self._front = (self._front+1)%len(self._data)
		self._size -= 1
		return answer

	def _resize(self,cap):
		old = self._data
		self._data = [None]*cap
		walk = self._front
		for k in old:
			self._data[k] = old[walk]
			walk = (walk+1)%len(old)
		self.front = 0

q = ArrayQueue()
print len(q)
print q.is_empty()
q.enqueue('dalakoti')
q.enqueue('jain')
q.enqueue('namit')
q.enqueue('varun')
q.enqueue('bohra')
print q.dequeue()
print q.dequeue()
print q.dequeue()
print q.dequeue()
print q.dequeue()

	
