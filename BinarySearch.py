"""
Recursive Approach to the Binary Search
Recursion is part of many different algorithmic programming solutions.
Binary Search Works well in sorted List. It works on logarithmic time or O(log n)
"""
def search(searchList, key):
  mid = int(len(searchList)/2)
  print("Searching midpoint at ",str(searchList[mid]))
  if mid == 0:
    """
    always provide an escape method for the recursion or the stack will fill, resulting in an error message. 
    In this case, the escape occurs when mid == 0, which means that there is no more searchList to search. 
    """
    print("No key found")
    return key
  elif key == searchList[mid]:
    print("Key found")
    return searchList[mid]
  elif key > searchList[mid]:
    print("SearchList now Contains ", str(searchList[mid:len(searchList)]))
    search(searchList[mid:len(searchList)], key)
  else:
    print("SearchList now Contains ", str(searchList[0:mid]))
    searchList(searchList[0:mid], key)

aList = list(range(1,1000))
search(aList, 567)
