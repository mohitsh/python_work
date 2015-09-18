

i = raw_input().split()
arri = [int(x) for x in i]

arrn = []
for i in range(arri[0]):
	n = raw_input().split()
	arr = [int(x) for x in n]
	arrn.append(arr)

k = int(raw_input())
#print arrn
#print k

for i in range(len(arrn)-1,0,-1):
	for j in range(i):
		if arrn[j][k] > arrn[j+1][k]:
			arrn[j],arrn[j+1] = arrn[j+1],arrn[j]

for line in arrn:
	line2 = " ".join(str(x) for x in line)
	print line2

