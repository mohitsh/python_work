

import Queue as Q

q = Q.PriorityQueue()
q.put(10)
q.put(3)
q.put(5)

while not q.empty():
	print q.get()
