
# Python Binary Search Recursive and iterative:

'''In a binary search, we divide a collection of elements into two halves to reduce the comparisons
for finding an element. The elements in the array must be sorted'''

# Binary search Algorithm

'''The binary search algorithm find index of a particular element in the list. It is one of the fastest algorithm'''

# steps in a binary search

'''
1- In a sorted array find the middle element
2- Compare x with the middle element.
3- if x equals the middle element, then the middle index is returned. Otherwise, the x will be compared with the middle
item.
4- Else if x is greater than the middle item, then it will be compare to the right side elements index
5- Else if x is less than the mid element, then x will be compared to the left side elements of the index.
6- we will choose either algorithm to run for the half to the list or the left half of the list of items.'''

# Recursive Method
'''The recursive method follows the divide and conquer approach: one function calls itself repeatedly until an element
is found in the list.'''
#
def binary_search(array, low, high, x):

    if high >= low:
        mid = (high + low) // 2

        if array[mid] == x:
            return mid

        elif array[mid] > x:
            return binary_search(array, low, mid - 1, x)

        else:
            return binary_search(array, mid + 1, high, x)

    else:
        return - 1

array = [2, 4, 6, 8, 20, 40, 60, 80]
x = 60

result = binary_search(array, 0, len(array)-1, x)

if result != -1:
    print("The index of the element is", str(result))
else:
    print("This element is not present in your array")

# Iterative Method for binary search
'''We use while loop in the iterative method to find the index position of an element. A set of statements will be 
repeated multiple times in iterative implementation'''

def iter_bina_search(array, x):
    low = 0
    high = len(array) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2

        if array[mid] < x:
            low = mid + 1

        elif array[mid] > x:
            high = mid - 1

        else:
            return mid

    return - 1

array = [2, 4, 6, 8, 20, 40, 60, 80]
x = 10

result = iter_bina_search(array, x)

if result != -1:
    print("The index of the element in the iterative method is: ", str(result))
else:
    print('Element not in the array')