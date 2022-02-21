# def search( nums, target):
#     left = 0
#     right = len(nums) - 1
#
#     while left <= right:
#         mid = (left + right) // 2
#         if nums[mid] == target:
#             return mid
#         elif target < nums[mid]:
#             right = mid - 1
#         else:
#             left = mid + 1
#     return -1
#
#
# if __name__=='__main__':
#     nums = [-1, 0, 3, 5, 9, 12]
#     target = 12
#     print(search(nums, target))

# Binary search of an ordered list
# test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42]
'''We have a list called test_list with ordered elements, using binary search find t=3 and t=13'''

'''Given an array of integers named test_list which is sorted in ascending order, and an integer t, write a function to search
t in test_list. If t exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.'''















