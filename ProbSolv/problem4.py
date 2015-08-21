
def mat_diag_sumMax(n,mat):
	left_diag = 0
	for i in range(n):
		left_diag = left_diag + mat[i][i]
	right_diag = 0
	
	for j in range(n):
		right_diag = right_diag + mat[j][n-1-j]
	
	return abs(left_diag-right_diag)
	#print left_diag
	#print right_diag




n = int(raw_input())
final = []
for i in range(n):
	arr = raw_input().split()
	num_arr = [int(x) for x in arr] 
	final.append(num_arr)

#print final    
print mat_diag_sumMax(n,final)                     
