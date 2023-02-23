#Here we declare and assign quicksort for performing
def quicksort(arr,lb,ub):
    if(lb<ub):
        loc = partition(arr,lb,ub)
        quicksort(arr,lb,loc-1)
        quicksort(arr,loc+1,ub)
    return arr


#Here we perform operation on partition formed from quicksot 
def partition(arr, lb,ub):
    pivot=arr[lb]
    low = lb
    high = ub
    while(low<high):
        while(arr[low]<=pivot and low <= high):
            low+=1
        while(arr[high]>pivot):
            high-=1
        if(low<high):
            arr[low],arr[high]=arr[high],arr[low]
    arr[high],arr[lb]=arr[lb],arr[high]

    return high

n = int(input("Enter the no. of inputs?"))
arr=[]
for i in range(n):
    arr.insert(i,int(input("")))
print("The sorted data is:",quicksort(arr,0,n-1))

