

# What is a tree?
# A Tree is a data structure that have a root node and each node can have any number of children
# Each node except the root has one or must has one parent only, a node can not be its own parent
# Node are associated with data
# One of the most used tree is the binary tree
# In the binary tree each node has at most, two children: left and right
# Each node has a numeric value value associated with it, children to the left must have lesser values than their parents
# Children to the right must have greater values than their parents.
# A tree cannot have duplicated value each value must be unique

# Create a Basic tree

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self, root):
        self.root = root



node = Node(10)

node.left = Node(5)
node.right = Node(15)

node.left.left = Node(2)
node.left.right = Node(6)

node.right.left = Node(13)
node.right.right = Node(10000)

myTree = Tree(node)

#print(myTree.name)
print(myTree.root.left.data)

print(myTree.root.right.right.data)




