"""排序函数库"""

def insert_downsort(a):
    """插入排序,递减"""
    for j in range(1,len(a)):
        key = a[j]
        i = j-1

        while i >= 0 and a[i] < key:
            a[i+1] = a[i]
            i = i-1

        a[i+1] = key
    return a

def insert_upsort(a):
    """插入排序,递增"""
    for j in range(1,len(a)):
        key = a[j]
        i = j-1

        while i >= 0 and a[i] > key:
            a[i+1] = a[i]
            i = i-1

        a[i+1] = key
    return a