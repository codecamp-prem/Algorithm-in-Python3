"""
The Quicksort is one of the fastest methods of sorting data. 

The average sort time of a Quicksort is O(n log n), but the worst-case sort time is O(n^2).

The first part of the task is to partition the data. 
The code chooses a pivot point that determines the left and right side of the sort. 

Quicksort can have a worst-case sort time of O(n2) when one of these events occurs:
• The dataset is already sorted in the desired order.
• The dataset is sorted in reverse order.
• All the elements in the dataset are the same.

Fortunately, using the right programming technique can mitigate these problems
by defining something other than the leftmost or rightmost index as the pivot point. 
The techniques that modern Quicksort versions rely on include:
• Choosing a random index
• Choosing the middle index of the partition
• Choosing the median of the first, middle, and last element of the partition for the
pivot (especially for longer partitions)

"""

data = [9, 5, 7, 4, 2, 8, 1, 10, 6, 3]

def partition(data,left,right):
    pivot = data[left]
    leftIndex = left + 1
    rightIndex = right
    
    while True:
        while leftIndex <= rightIndex and data[leftIndex] <= pivot:
            leftIndex += 1
        while rightIndex >=leftIndex and data[rightIndex] >= pivot:
            rightIndex -= 1
        if rightIndex <= leftIndex:
            break
        data[leftIndex],data[rightIndex] = data[rightIndex], data[leftIndex]
        print(data)
        
    data[left],data[rightIndex] = data[rightIndex], data[left]
    print(data)
    return rightIndex

def quickSort(data, left, right):
    if right <= left:
        return
    else:
        pivot = partition(data,left,right)
        quickSort(data, left, pivot-1)
        quickSort(data, pivot+1, right)
    
    return data

quickSort(data, 0 , len(data)-1)

"""
O/P:
-----

[9, 5, 7, 4, 2, 8, 1, 3, 6, 10]
[6, 5, 7, 4, 2, 8, 1, 3, 9, 10]
[6, 5, 3, 4, 2, 8, 1, 7, 9, 10]
[6, 5, 3, 4, 2, 1, 8, 7, 9, 10]
[1, 5, 3, 4, 2, 6, 8, 7, 9, 10]
[1, 5, 3, 4, 2, 6, 8, 7, 9, 10]
[1, 2, 3, 4, 5, 6, 8, 7, 9, 10]
[1, 2, 3, 4, 5, 6, 8, 7, 9, 10]
[1, 2, 3, 4, 5, 6, 8, 7, 9, 10]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

"""
