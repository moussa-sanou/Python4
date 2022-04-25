
# Tree balancing

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

    def add(self, data):
        if data == self.data:
            # Binary search tree doesnt contain duplicates
            return

        if data < self.data:
            if self.left is None:
                self.left = Node(data)
                return
            else:
                self.left.add(data)

        if data > self.data:
            if self.right is None:
                self.right = Node(data)
                return
            else:
                self.right.add(data)

    def findMin(self):
        if self.left:
            return self.left.findMin()
        return self

    def delete(self, data):
        if self.data == data:
            if self.right and self.left:
                minimuValue = self.right.findMin()
                self.data = minimuValue.data
                self.right = self.right.delete(minimuValue.data)
                return self
            else:
                return self.right or self.left

        if self.right and data > self.data:
            self.right = self.right.delete(data)

        if self.left and data < self.data:
            self.left = self.left.delete(data)
        return self




class Tree:
    def __init__(self, root):
        self.root = root

    def search(self, target):
        return self.root.search(target)

    def add(self, data):
        return self.root.add(data)

    def delete(self, data):
        self.root = self.root.delete(data)