
def puzzle_solve(k,s,u):
	for ch in u:
		s.append(ch)
		u.remove(ch)
		if k == 1:
			print s
		else:
			puzzle_solve(k-1,s,u)
		
		entry = s.pop()
		u.append(entry)

k = 3
s = []
u = ['a','b','c']
puzzle_solve(k,s,u)
