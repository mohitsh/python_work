
a = [[1,2,3,4,5],[5,4,3,2,1],[6,7,8,9,0],[0,9,8,7,6]]

rows = len(a)
cols = len(a[0])

for j in range(cols):
	for i in range(rows):
		print a[i][j],
	print "\n"
