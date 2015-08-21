



def arr_sum(n,arr):
    var_sum = 0
    for i in range(n):
        var_sum = var_sum + arr[i]
    return var_sum

n = int(raw_input())
arr = raw_input().split()
num_arr = [int(x) for x in arr]
print arr_sum(n,num_arr)
