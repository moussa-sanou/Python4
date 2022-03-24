class queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        '''Takes in an item and insert that item into the 0th index of the list that is representing the queueself.
        The runtime is O(n) or linear time, because inserting into the 0th index of a list forces all the other items in
        the list to move one index to the right.'''
        self.items.insert(0, item)

    def dequeue(self):
        '''Retruns and remove the front most item of the queue, which is represented by the last item in the list
        The runtime is O(1), or constant time because indexing to the end of a list happens in constant time.'''
        if self.items:
            return self.items.pop()
        return None

    def peek(self):
        pass

    def size(self):
        pass

    def is_empty(self):
        pass

my_q = queue()
my_q.dequeue()
my_q.items
print(my_q.items)
