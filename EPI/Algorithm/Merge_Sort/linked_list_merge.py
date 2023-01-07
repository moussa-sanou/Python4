

def merge_sort(linkedList):
    '''Sorts a linked list in ascending order
    Recursively divide the linked list into sublists containing a single node
    Repeatedly merge the sublists to produce sorted sublists until one remains
    Returns a sorted linked list'''

    if linkedList.size() == 1:
        return linkedList
    elif linkedList.head is None:
        return linkedList

    left_half, right_half = split(linkedList)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)

def split(linked_list):
    '''Divide the unsorted list at midpoint into sublists'''

    if linked_list == None or linked_list.head == None:
        left_half = linked_list
        right_half = None
        return left_half, right_half
    else:
        size = linked_list.size()

