def getMinMax(a,n):
    min=a[0]
    max=a[0]
    for i in range(1,n):
        if a[i]>max:
            max=a[i]
        if a[i]<min:
            min=a[i]
    return min,max 