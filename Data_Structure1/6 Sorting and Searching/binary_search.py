
# Binary search of an ordered list
# test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42]
'''We have a list called test_list with ordered elements, using binary search find t=3 and t=13'''

def search_t(test_list, t, low=None, high=None):

    if low is None: # Find the lower element in our list
        low = 0
    if high is None: # Find the highest element in our list
        high = len(test_list) - 1
    if low > high: # If element not in the list return - 1
        return - 1
    # Find the midpoint or middle of our list
    mid = (low + high) // 2

    if t == test_list[mid]: # If the element we are searching for is the mid element of the return the mid index
        return mid
    # Search at the left side of our mid element
    elif t < test_list[mid]:
        new_high = mid - 1
        return search_t(test_list, t, low, new_high)
    # search at the right side of the mid element
    else:
        new_low = mid + 1
        return search_t(test_list, t, new_low, high)

test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42]
t = 8
print(search_t(test_list, t))
