
def merge(l,r,a):
    nl = len(a)/2
    nr = len(a) - len(a)/2
    i = 0
    j = 0
    k = 0
    while(i<nl and j <nr):
        if(l[i]<=r[i]):
            a[k] = l[i]
            k = k+1
            i = i+1
        else:
            a[k] = r[j]
            k = k+1
            j = j+1
    while(i<nl):
        a[k] = l[i]
        k = k+1
        i = i+1
    while(j<nr):
        a[k] = r[j]
        k = k+1
        j = j+1
    return a
    
def merge_sort(a):
    n = len(a)
    if(n<2):
        return n
    mid = n/2
    left = []
    right = []
    for i in range(0,n/2):
        left.append(a[i])
    for j in range(n/2,n):
        right.append(a[j])

    merge_sort(left)
    merge_sort(right)
    merge(left,right,a)            
    return a 