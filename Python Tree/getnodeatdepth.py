class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def search(self, target):
        if self.data == target:
            print("Found it!")
            return self

        if self.left and self.data > target:
            return  self.left.search(target)

        if self.right and self.data < target:
            return self.right.search(target)

        print("Value is not in tree")

    def getNodesAtDepth(self, depth, nodes=[]):
        if depth == 0:
            nodes.append(self.data)
            return nodes

        if self.left:
            self.left.getNodesAtDepth(depth-1, nodes)
        else:
            nodes.extend([None]*2**(depth-1))

        if self.right:
            self.right.getNodesAtDepth(depth-1, nodes)
        else:
            nodes.extend([None]*2**(depth-1))
        return nodes



class Tree:
    def __init__(self, root, name=''):
        self.root = root
        self.name = name

    def search(self, target):
        return self.root.search(target)

    def getNodesAtDepth(self, depth):
        return self.root.getNodesAtDepth(depth)

tree = Tree(Node(50), 'Get all nodes at depth')
tree.root.left = Node(25)
tree.root.right = Node(75)
tree.root.left.left = Node(13)
tree.root.left.right = Node(35)
tree.root.right.left = Node(55)
tree.root.right.right = Node(103)
tree.root.left.left.left = Node(2)
tree.root.left.left.right = Node(20)
tree.root.right.left = Node(55)
tree.root.right.right.right = Node(256)

print(tree.getNodesAtDepth(2))