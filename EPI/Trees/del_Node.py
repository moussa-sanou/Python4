
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def search(self, target):
        if self.data == target:
            print('found it')
            return self

        if self.left and self.data > target:
            return self.left.search(target)

        if self.right and self.data < target:
            return self.right.search(target)

        print('Target value not in the Tree')

    def add(self, new_data):
        if self.data == new_data:
            return

        if new_data < self.data:
            if self.left is None:
                self.left = Node(new_data)
                return
            else:
                self.left.add(new_data)

        if new_data > self.data:
            if self.right is None:
                self.right = Node(new_data)
                return
            else:
                self.right.add(new_data)

    # Delete a node following the RTFM approach (Right Tree Find Minimum: RTFM)
    def findMin(self):
        if self.left:
            return self.left.findMin()
        return self.data

    def delete(self, target):
        if self.data == target:
            #Do the deletion here
            if self.left and self.right:
                # Right Tree Find Minimum(RTFM)
                minValue = self.right.findMin()
                self.data = minValue
                self.right = self.right.delete(minValue)
            else:
                return self.left and self.right

        if self.right and target > self.data:
            self.right = self.right.delete(target)

        if self.left and target < self.data:
            self.left = self.left.delete(target)

        return self



class Tree:
    def __init__(self, root):
        self.root = root

    def search(self, target):
        return self.root.search(target)

    def add(self, new_data):
        return self.root.add(new_data)

    def delete(self, target):
        self.root = self.root.delete(target)

tree = Tree(Node(50))
tree.root.left = Node(25)
tree.root.right = Node(75)
tree.add(10)
tree.add(76)

print(tree.root.right.right.data)


