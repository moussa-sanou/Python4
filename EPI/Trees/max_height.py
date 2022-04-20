
# Find the maximum height of a tree

class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

    def search(self, target):
        if self.data == target:
            print('found it ')
            return self

        if self.right  and  self.data < target:
            return self.right.search(target)

        if  self.left and self.data > target:
            return self.left.search(target)

        print('Not found')

    def height(self, h=0):
        leftheight = self.left.height(h+1) if self.left else h
        rightHeight = self.right.height(h+1) if self.right else h
        return max(leftheight, rightHeight)



class Tree:
    def __init__(self, root):
        self.root = root

    def search(self, target):
        return self.root.search(target)

    def height(self):
        return self.root.height()



tree = Tree(Node(50))
tree.root.left = Node(25)
tree.root.right = Node(75)
tree.root.left.left = Node(10)
tree.root.left.right = Node(35)
tree.root.left.right.left = Node(30)
tree.root.left.right.right = Node(42)
tree.root.left.left.left = Node(5)
tree.root.left.left.right = Node(13)
tree.root.left.left.left.left = Node(2)

print(tree.height())

print('-----' * 10)
print('A very short Tree')
tree = Tree(Node(50))
print(tree.height())