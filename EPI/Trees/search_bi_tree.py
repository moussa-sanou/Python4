
# Binary search tree implementation

# Create a Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def search(self, target):
        if self.data == target:
            print('found it ')
            return self

        if self.left and self.data > target:
            return self.left.search(target)

        if self.right and self.data < target:
            return self.right.search(target)

        print('Not Found')

class Tree:
    def __init__(self, root, name = ''):
        self.root = root
        self.name = name

    def search(self, target):
        return self.root.search(target)


node = Node(10)

node.left = Node(5)
node.right = Node(15)

node.left.left = Node(2)
node.left.right = Node(6)

node.right.left = Node(13)
node.right.right = Node(20000)

myTree = Tree(node, 'Sami\'s')

found = myTree.search(10000)

print(found.data)


