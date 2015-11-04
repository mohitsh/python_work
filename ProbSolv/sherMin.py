
def sher_min(arr,n,p,q):
    arr1 = []
    cool = []
    for i in range(p,q+1):
        arr2 = []
        for j in range(n):
            arr2.append(abs(arr[j]-i))
        cool.append(min(arr2))
        arr1.append(i)
    
    dude = max(cool)
    ind = cool.index(dude)
    #print cool
    #print arr1
    print arr1[ind]
    


n = int(raw_input())
a = raw_input().split()
a = [int(x) for x in a]
p_q = raw_input().split()
p_q = [int(x) for x in p_q]
p = p_q[0]
q = p_q[1]

sher_min(a,n,p,q)
