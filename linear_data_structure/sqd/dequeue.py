class ArrayDeQueue:
	
	default_capacity = 10
	def __init__(self):
		self._front = 0
		self._data = [None]*ArrayDeQueue.default_capacity
		self._size = 0

	def __len__(self):
		return self._size

	def is_empty(self):
		return self._size == 0

	def first(self):
		return self._data[self._front]

	def add_last(self,e):
		if len(self._data) == self._size:
			self._resize(2*len(self._data))
		avail = (self._front + self._size)%len(self._data)
		self._data[avail] = e
		self._size += 1

	def delete_first(self):
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

	def last(self):
		back = (self._size - 1 + self._front) % len(self._data)
		return self._data[back]

	def add_first(self,e):
		if self._size == len(self._data):
			_resize(2*len(self._data))
		
		self._front = (self._front-1)%len(self._data)
		self._data[self._front] = e
		self._size += 1

	def delete_last(self):
		avail = (self._front + self._size) %len(self._data)
		answer = self._data[avail]
		self._data[avail] = None
		self._size -= 1
		return answer


q = ArrayDeQueue()
print len(q)
print q.is_empty()
print q.first()
q.add_last('dalakoti')
q.add_last('mohit')
q.add_last('jain')
q.add_last('tapan')
q.add_last('varun')
q.add_last('bohra')
print len(q)
print q.is_empty()
print q.first()
q.delete_first()
q.delete_first()
q.delete_first()
q.delete_first()
print len(q)
print q.first()
print q.is_empty()
print q.last()
q.add_first('dude')
print q.first()
q.add_first('jangid')
print len(q)
print q.first()
print q.last()
q.delete_last()
print len(q)
print q.last()



