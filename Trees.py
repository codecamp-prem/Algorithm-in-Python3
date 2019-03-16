class BinaryTree:
    def __init__(self, nodeData, left=None, right=None):
        self.nodeData = nodeData
        self.left = left
        self.right = right
        
    def __str__(nodeData):
        return str(self.nodeData)
    
tree = BinaryTree("Root")
BranchA = BinaryTree("Branch A")
BranchB = BinaryTree("Branch B")

tree.left = BranchA
tree.right = BranchB

leafC = BinaryTree("Leaf C")
leafD = BinaryTree("Leaf D")
leafE = BinaryTree("Leaf E")
leafF = BinaryTree("Leaf F")

BranchA.left = leafC
BranchA.right = leafD

BranchB.left = leafE
BranchB.right = leafF

"""
# Traversing the tree #

Traversing the tree means checking the links and verifying that
they actually do connect as you think they should.
"""

def traverse(tree):
    if tree.left != None:
        traverse(tree.left)
    if tree.right != None:
        traverse(tree.right)
    print(tree.nodeData)
    
traverse(tree)

"""
O/P:

Leaf C
Leaf D
Branch A
Leaf E
Leaf F
Branch B
Root    
    
As the output shows, the traverse function doesn’t print anything until it gets to
the first leaf. It then prints both leaves and the parent of those leaves. The traversal
follows the left branch first, and then the right branch. The root node comes last.
"""
