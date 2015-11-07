

import Queue as Q
import heapq

q = Q.PriorityQueue()
q.put((13,'dalla'))
q.put((2,'kutta'))
q.put((30,'bohra'))

while not q.empty():
	print q.get()


heap = []
heapq.heappush(heap,(12,'one'))
heapq.heappush(heap,(2,'two'))
heapq.heappush(heap,(30,'three'))
heapq.heappush(heap,(4,'four'))

for x in heap:
	print x
