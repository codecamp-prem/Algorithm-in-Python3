"""
The selection sort replaced a predecessor, the bubble sort, because it tends to provide
better performance than the bubble sort. 
Even though both sorts have a worst-case sort speed of O(n^2), the selection sort performs fewer exchanges. 
A selection sort works in one of two ways: 
  It either looks for the smallest item in the list and places it in the front of the list 
  (ensuring that the item is in its correct location) or 
  looks for the largest item and places it in the back of the list. 
Either way, the sort is exceptionally easy to implement and 
guarantees that items immediately appear in the final location once moved 
(which is why some people call it an in-place comparison sort). 
"""
data = [9, 5, 7, 4, 2, 8, 1, 10, 6, 3]

for scanIndex in range(0, len(data)):
    minIndex = scanIndex

    for compIndex in range(scanIndex + 1, len(data)):
        if data[compIndex] < data[minIndex]:
            minIndex = compIndex

    if minIndex != scanIndex:
        data[scanIndex], data[minIndex] = \
        data[minIndex], data[scanIndex]
        print(data)
"""
O/P
----

[1, 5, 7, 4, 2, 8, 9, 10, 6, 3]
[1, 2, 7, 4, 5, 8, 9, 10, 6, 3]
[1, 2, 3, 4, 5, 8, 9, 10, 6, 7]
[1, 2, 3, 4, 5, 6, 9, 10, 8, 7]
[1, 2, 3, 4, 5, 6, 7, 10, 8, 9]
[1, 2, 3, 4, 5, 6, 7, 8, 10, 9]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

"""
