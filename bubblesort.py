def bubble_sort(arr,n):
    for i in range(0,n-1):
        flag = 0
        for j in range(0,n-1):
            if (arr[j]>arr[j+1]):
                # temp=arr[j]
                # arr[j]=arr[j+1]
                # arr[j+1]=temp
                flag=1
                arr[j],arr[j+1]=arr[j+1],arr[j]
        if (flag == 0):
            break
    return arr
arr=[]
n = int(input("Enter the number of inputs?"))
for i in range(0,n):
    arr.insert(i,int(input("")))
print("Bubble Sorted Data is:",bubble_sort(arr,n))

