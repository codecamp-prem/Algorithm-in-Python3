"""
A stack provides last in/first out (LIFO) data storage.
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
        
