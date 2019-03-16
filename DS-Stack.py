"""
Sub: Stack implementation in Python

A stack provides last in/first out (LIFO) data storage.
-----------------------------

Python lists are ordered lists of data values that are easy and intuitive to use. 
From an algorithm perspective, they often don’t perform well because they store the list
elements in computer memory and access them using an index and memory pointers
(a number that provides the memory address of the data). 
They work exactly the way a book index or a package does. 
Lists don’t have knowledge of their content. 

When your application makes a data request,
                    the list scans through all its items,which is even slower. 
When data is scattered across your computer’s memory, 
                    lists must gather the data from each location individually and slowing access more.

"""
MyStack = []
StackSize = 3

def DisplayStack():
    print("Stack Currently Contains: ")
    for Item in MyStack:
        print(Item)

def PushInStack(value):
    if len(MyStack) < StackSize:
        MyStack.append(value)
    else:
        print('Stack already Full')
        
def PopOutStack():
    if len(MyStack) > 0:
        print('Popping Out: ',MyStack.pop())
    else:
        print('Stack is Empty')
        
