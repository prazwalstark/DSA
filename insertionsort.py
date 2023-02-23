def insertionsort(arr,n):
    for i in range (1,n):
        temp = arr[i]
        j = i-1
        while(j>=0 and arr[j]>temp):
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=temp
    return arr
			
arr = []
n = int(input("Enter the no. of data?"))
for i in range(n):
    arr.append(int(input("")))
print("The sorted data is:",insertionsort(arr,n))
	

