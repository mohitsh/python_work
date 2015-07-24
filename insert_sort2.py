def insert_sort(a):
    for i in range(1,len(a)):
        position = i
        current_value = a[i]

        while position > 0 and a[position-1] > current_value:
            a[position] = a[position - 1]
            position = position - 1

        a[position] = current_value

    return a

a = [134,466,234,656,977,566,345,979,234,465,123]
print 'original array'
print a

insert_sort(a)
print 'modified array'
print a
            
