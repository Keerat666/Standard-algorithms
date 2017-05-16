def quicksort(myList, start, end):
    if start < end:

        pivot = partition(myList, start, end)

        quicksort(myList, start, pivot-1)
        quicksort(myList, pivot+1, end)
    return myList

def partition(myList, start, end):
    pivot = myList[start]
    left = start+1
    right = end
    done = False
    while not done:
        while left <= right and myList[left] <= pivot:
            left = left + 1
        while myList[right] >= pivot and right >=left:
            right = right -1
        if right < left:
            done= True
        else:
            myList[left],myList[right]=myList[right],myList[left]

    temp=myList[start]
    myList[start]=myList[right]
    myList[right]=temp
    return right


x=int(input("Enter the length of the list"))
a=0;
l={};
while(a<x):
    l[a]=input("");
    a=a+1

quicksort(l,0,x-1)
i=0;
while i< x:
    print (l[i])
    i=i+1


