def selectionsort(arr,n):
    for i in range(n-1):
        temp = i
        for j in range(i+1,n):
            if (arr[temp]>arr[j]):
                temp = j
        arr[i],arr[temp]=arr[temp],arr[i]
    return arr

arr=[]
n = int(input("Enter the number of inputs?"))
for i in range(n):
    arr.append(int(input("")))
print("Sorted Data is:",selectionsort(arr,n))

    
