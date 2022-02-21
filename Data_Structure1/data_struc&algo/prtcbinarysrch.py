# # Binary search pratice
#
# '''Binary implementation'''
#
# def binary_search(list1, target, low=None, high=None):
#     if low is None:
#         low = 0
#     if high is None:
#         high = len(list1) - 1
#     # After initializing the high and low of our list we need to find the middle
#     middle = (low + high) // 2
#
#     # Set up our search
#     '''This function will be called if the search element is not in the list'''
#     '''If the item we are looking for is not in our list return -1'''
#     if high < low:
#         return -1
#
#     '''if the item we are looking for in the middle of our list return the middle index number'''
#     if list1[middle] == target:
#         return middle
#
#     '''If the item we are looking for is not the middle item of the list, look at the left side of the middle'''
#     if target < list1[middle]:
#         #Set a new high at the left side of the list
#         new_high = middle - 1
#         return binary_search(list1, target, low, new_high)
#
#     # '''if the items we are looking for not in the left side of the list, look at the right side'''
#     else:
#         '''set a new low in the right side of the list'''
#         new_low = middle + 1
#         return binary_search(list1, target, new_low, high)
#
# if __name__== '__main__':
#     list1 = [2, 4, 6, 8, 20, 40, 60, 80]
#     target = int(input("Please Enter the item you are looking for: "))
#     result = binary_search(list1, target)
#
#
#     if result != - 1 :
#         print("The item you are looking for is store at index: ", result)
#     else:
#         print('The item you are looking for is not in the list')


#
# def search(nums, target, low=None, high=None):
#     if low is None:
#         low = 0
#     if high is None:
#         high = len(nums) - 1
#     if high < low : # if the element we are looking for not in the list return -1
#         return - 1
#     # Find the middle of our array
#     middle = (low + high) // 2
#     # Binary search implementation
#     if target == nums[middle]:
#         return middle
#     elif target < nums[middle]:
#         new_high = middle - 1
#         return search(nums, target, low, new_high)
#     else:
#         new_low = middle + 1
#         return search(nums, target, new_low, high)
# if __name__=='__main__':
#     #nums = [2, 3, 5, 7, 9]
#     nums = [1, 4, 5, 8, 9]
#     target = int(input('Enter the element you are looking for: '))
#     result = search(nums, target)
#
#     if result != - 1 :
#         print('Element found at index ', result)
#     else:
#         print('Element not found')


'''Given a sorted array of n integers and target value, determine if the target exist in the array in logarithmic time
using the binary search algorithm. if target exists in the array, print the index of it
nums[] = [2, 3, 5, 7, 9]
target = 7
output: element found at index 3
input:
mums[] = [1, 4, 5, 8, 9]
target = 2
output: Element not found'''

#
# def search_target(nums, target, left=None, right=None):
#     if left is None:
#         left = 0
#     if right is None:
#         right = len(nums) - 1
#     if left > right:
#         return - 1
#     # Start the binary search find the middle of the list
#     middle = (left + right) // 2
#
#     if target == nums[middle]:
#         return middle
#     elif target < right:
#         new_right = middle - 1
#         return search_target(nums, target, left, new_right )
#     else:
#         new_left = middle + 1
#         return search_target(nums, target, new_left, right)
#
# if __name__=='__main__':
#     nums = [1, 4, 5, 8, 9]
#     target = 5
#     search_result = search_target(nums, target)
#
#     if search_result != -1:
#         print('Element Found at index: ', search_result)
#     else:
#         print('Element not found')

'''Suppose you have the following sorted list1 = [3, 5, 6, 8, 11, 12, 14, 15, 17, 18] and are using the 
 recursive binary search algorithm. find the key 8'''

def search_key (list1, key, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(list1) - 1
    if low > high:
        return - 1
    # Let's start the binary search
    # Find the middle of our list
    middle = (low + high) // 2

    if key == list1[middle]:
        return middle
    # Search the left side of the middle of our list
    elif key < list1[middle]:
        new_high = middle - 1
        return search_key(list1, key, low, new_high)
    else:
        new_low = middle + 1
        return search_key(list1, key, new_low, high)

if __name__ == '__main__':
    list1 = [3, 5, 6, 8, 11, 12, 14, 15, 17, 18]
    key = 0
    result = search_key(list1, key)

    if result != - 1:
        print('the element is found at: ', key)
    else:
        print('Element not found')


