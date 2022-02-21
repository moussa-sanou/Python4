# Binary search explain

def binary_search(mylist, target, low=None, high=None ): # Defined a function with high and low initialized as none
    if low is None:
        low = 0
    if high is None:
        high = len(mylist) - 1 #Find the lenght of the list minus -1

    if high < low: # if we reach a condition where the high < low it means the item is not in the list
        return -1

    # Getting the middle or midpoint of our list
    middle = (low + high) // 2  # we define how the middle of the is supposed to be found

    if mylist[middle] == target: # Is the item we are searching in list the middle item? if yes return the item if not move to the next condition.
        return middle

    elif target < mylist[middle]:  # If the above condition not True search at the left side of the middle.
        new_high = middle - 1 # Find a new high in the left side of midpoint
        return binary_search(mylist, target, low, new_high) # return the search result if the target if found

    else:
        '''target > mylist[middle]'''
        new_low = middle + 1
        return binary_search(mylist, target, new_low, high)



if __name__ == '__main__':
    mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target = 9
    search_result = binary_search(mylist, target)
    if search_result != - 1:
        print("The index of the element you are searching for is: ", search_result)
    else:
        print("Item not in the list")



