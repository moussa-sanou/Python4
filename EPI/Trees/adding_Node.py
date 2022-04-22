
# Adding a new node to a tree

class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

    def search(self, target):
        if self.data == target:
            print('found it')
            return self

        if self.right and self.data < target: # If the target value is greater than root value search right
            return self.right.search(target)

        if self.left and self.data > target: #if the target value is less than the root value search left
            return self.right.search(target)

    def height(self, h=0):
        leftheight = self.left.height(h+1) if self.left else h
        rightHeight = self.right.height(h+1) if self.right else h
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

    def add(self, data):
        if data == self.data:
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

class Tree:
    def __init__(self, root, name=''):
        self.root = root
        self.name = name

    def search(self, target):
        return self.root.search(target)

    def add(self, data):
        self.root.add(data)

    def height(self):
        return self.root.height()

    def getNodesAtDepth(self, depth):
        return self.root.getNodesAtDepth(depth)

    def _nodeToChar(self, n, spacing):
        if n is None:
            return '_' + (' ' * spacing)
        spacing = spacing - len(str(n)) + 1
        return str(n) + (' ' * spacing)

    def print(self, label=''):
        print(self.name + ' ' + label)
        height = self.root.height()
        spacing = 3
        width = int((2 ** height - 1) * (spacing + 1) + 1)
        # Root offset
        offset = int((width - 1) / 2)
        for depth in range(0, height + 1):
            if depth > 0:
                # print directional lines
                print(' ' * (offset + 1) + (' ' * (spacing + 2)).join(
                    ['/' + (' ' * (spacing - 2)) + '\\'] * (2 ** (depth - 1))))
            row = self.root.getNodesAtDepth(depth, [])
            print((' ' * offset) + ''.join([self._nodeToChar(n, spacing) for n in row]))
            spacing = offset + 1
            offset = int(offset / 2) - 1
        print('')

tree = Tree(Node(50))
tree.root.left = Node(25)
tree.root.right = Node(75)
tree.add(10)
tree.add(76)
tree.print()



