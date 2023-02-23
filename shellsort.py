def shellsort(arr,n):
    gap = n//2
    while (gap >=1):
        for j in range(gap,n,1):
            i = j-gap
            while (i>=0):
                    if(arr[i]<arr[j]):
                        break
                    else:
                        arr[j],arr[i]=arr[i],arr[j]
                    i-=gap            
        gap = gap //2
    return arr


arr=[]
n = int(input("Enter the number of inputs?"))
for i in range(n):
    arr.append(int(input("")))
print("Sorted Data is:",shellsort(arr,n))