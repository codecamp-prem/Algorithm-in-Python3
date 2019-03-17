"""
A Mergesort works by applying the divide and conquer approach. 
The sort begins by breaking the dataset into individual pieces and sorting the pieces. 
It then merges the pieces in a manner that ensures that it has sorted the merged piece.
The sorting and merging continues until the entire dataset is again a single piece.

The worst-case sort speed of the Mergesort is O(n log n), which makes it considerably
faster than the techniques used in the Insertion or Bubble Sort (because log n is
always smaller than n). 

This sort actually requires the use of two functions. 
The first function works recursively to split the pieces apart and put them back together again.
"""

data = [9, 5, 7, 4, 2, 8, 1, 10, 6, 3]

def mergeSort(list):
    # Determine whether List is broken into
    # individual pieces
    
    if(len(list) < 2):
        return list
    
    # Find the middle of the list
    middle = len(list)//2
    
    # Brak the list into two pieces
    left = mergeSort(list[:middle])
    right = mergeSort(list[middle:])
    
    # Merge two sorted piece into larger piece
    print("Left Side: ",left)
    print("Right Side: ", right)
    
    merged = merge(left, right)
    print("Merged ", merged)
    
    return merged

def merge(left, right):
    # When the left or right side is empty
    # it means that this is an individual iteam and is 
    # already sorted
    
    if not len(left):
        return left
    if not len(right):
        return right
    
    # Define variable used to merge two pieces .
    result = []
    leftIndex = 0
    rightIndex = 0
    totalLen = len(left) + len(right)
    
    # Keep working until all the items are merged
    while (len(result) < totalLen):
        # perform required comparision and merge
        # the pieces according to value
        if left[leftIndex] < right[rightIndex]:
            result.append(left[leftIndex])
            leftIndex+= 1
        else:
            result.append(right[rightIndex])
            rightIndex+= 1
            
        # when the left side and right side is longer,
        # add the remaining elements to result.
        if leftIndex == len(left) or rightIndex == len(right):
            result.extend(left[leftIndex:] or right[rightIndex:])
            break
        print('Result: ',result)
    return result

mergeSort(data)

"""
O/P:
---

Left Side:  [9]
Right Side:  [5]
Merged  [5, 9]

Left Side:  [4]
Right Side:  [2]
Merged  [2, 4]

Left Side:  [7]
Right Side:  [2, 4]
Result:  [2]
Merged  [2, 4, 7]

Left Side:  [5, 9]
Right Side:  [2, 4, 7]
Result:  [2]
Result:  [2, 4]
Result:  [2, 4, 5]
Merged  [2, 4, 5, 7, 9]

Left Side:  [8]
Right Side:  [1]
Merged  [1, 8]

Left Side:  [6]
Right Side:  [3]
Merged  [3, 6]

Left Side:  [10]
Right Side:  [3, 6]
Result:  [3]
Merged  [3, 6, 10]

Left Side:  [1, 8]
Right Side:  [3, 6, 10]
Result:  [1]
Result:  [1, 3]
Result:  [1, 3, 6]
Merged  [1, 3, 6, 8, 10]

Left Side:  [2, 4, 5, 7, 9]
Right Side:  [1, 3, 6, 8, 10]
Result:  [1]
Result:  [1, 2]
Result:  [1, 2, 3]
Result:  [1, 2, 3, 4]
Result:  [1, 2, 3, 4, 5]
Result:  [1, 2, 3, 4, 5, 6]
Result:  [1, 2, 3, 4, 5, 6, 7]
Result:  [1, 2, 3, 4, 5, 6, 7, 8]
Merged  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

"""
