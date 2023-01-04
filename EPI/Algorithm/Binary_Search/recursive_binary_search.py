'''A recursive function is a function which calls itself '''

'''The recyrsive binary search is slightly different from the regular binary search
it will return True is the value exist and False if it doesn't  instead of the index '''

def recursive_binary_search(list, target):
    if len(list) == 0:
        return False
    else:
        mid = (len(list)) // 2
        if list[mid] == target:
            return True
        else:
            if list[mid] < target:
                return recursive_binary_search(list[mid + 1:], target)
            else:
                return recursive_binary_search(list[:mid], target)

def verify(result):
    print("Target found: ", result)

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = recursive_binary_search(list, 12)
verify(result)

result = recursive_binary_search(list, 6)
verify(result)
