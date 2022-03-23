

class Stack(object):
    def __int__(self):
        self.items = []

    def push(self, item):
        '''Acceepts an item as a parameter and appends it to the end of the list. Returns nothing
        The runtime for this method is O(1), or constant time, because appending
        to the end of a list happens constant time'''

        self.items.append(item)

    def pop(self):
        pass

    def peek(self):
        pass

    def size(self):
        pass

    def is_empty(self):
        pass

if __name__=="__main__":

    my_stack = Stack()
    my_stack.push('apple')
    print( my_stack.push('apple'))

