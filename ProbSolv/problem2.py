



# Enter your code here. Read input from STDIN. Print output to STDOUT

def arr_sum(n,arr):
    sum = 0
    for i in range(n):
           sum = sum + arr[i]
    return sum


n = int(raw_input())
array = raw_input().split()
num_array = [int(x) for x in array]
print arr_sum(n,num_array)
