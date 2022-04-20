
# Get and print all the node at a particular height

class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

    def search(self, target):
        if self.data == target:
            print('found it')
            return self

        if self.left and self.data > target:
            return self.left.search(target)

        if self.right and self.data < target:
            return self.right.search(target)

        print('Not found')

    def height(self, h=0):
        leftheight = self.left.height(h + 1) if self.left else h
        rightHeight = self.right.height(h + 1) if self.right else h
        return max(leftheight, rightHeight)


    def getNodesAtDepth(self, depth, nodes=[]):
        if depth == 0:
            nodes.append(self.data)
            return nodes

        if self.left:
            self.left.getNodesAtDepth(depth-1, nodes)
        if self.right:
            self.right.getNodesAtDepth(depth-1, nodes)
        return nodes

class Tree:
    def __init__(self, root):
        self.root = root

    def search(self, target):
        return self.root.search(target)

    def getNodesAtDepth(self, depth):
        return self.root.getNodesAtDepth(depth)


tree = Tree(Node(50))
tree.root.left = Node(25)
tree.root.right = Node(75)
tree.root.left.left = Node(13)
tree.root.left.right = Node(35)
tree.root.left.right.right = Node(37)
tree.root.right.left = Node(55)
tree.root.right.right = Node(103)
tree.root.left.left.left = Node(2)
tree.root.left.left.right = Node(20)
tree.root.right.left = Node(55)
tree.root.right.right.right = Node(256)

print(tree.getNodesAtDepth(2))