import math


def mergesort(arr, lb, ub):
    if (lb < ub):
        mid = math.floor((lb+ub)/2)
        mergesort(arr, lb, mid)
        mergesort(arr, mid+1, ub)
        merge(arr, lb, mid, ub)
    return arr


def merge(arr, lb, mid, ub):
    b = {}
    i = lb
    j = mid+1
    k = lb
    while (i <= mid and j <= ub):
        if (arr[i] <= arr[j]):
            b[k] = arr[i]
            i += 1
        else:
            b[k] = arr[j]
            j += 1
        k += 1
    if (i > mid):
        while (j <= ub):
            b[k] = arr[j]
            j+=1
            k += 1
    else:
        while (i <= mid):
            b[k] = arr[i]
            i+=1
            k += 1

    for l in range(lb, ub+1):
        arr[l] = b[l]
    

n = int(input("Enter the no. of inputs?"))
arr=[]
for i in range(n):
    arr.append(int(input("")))
print("The sorted data is:",mergesort(arr,0,n-1))