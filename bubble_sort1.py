def bubble_sort(a):
    for moveon in range(len(a)-1,0,-1):
        for i in range(moveon):
            if a[i] > a[i+1]:
                tmp = a[i+1]
                a[i+1] = a[i]
                a[i] = tmp

    return a

a = [123,3254,436,234,45,56,234,56,76,56,234,56,756]
print a
bubble_sort(a)
print a
