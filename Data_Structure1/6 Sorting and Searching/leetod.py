'''Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search
target in nums. If target exists, then return its index. Otherwise, return -1. Input: nums = [-1,0,3,5,9,12], target = 9,
Output: 4
target = 2
Output: -1
'''


def search(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if target == nums[mid]:
            return mid
        elif target < nums[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1


nums = [-1,0,3,5,9,12]
target = 0

print(search(nums, target))


'''Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return 
the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
Input: nums = [1,3,5,6], target = 5
Output: 2
Input: nums = [1,3,5,6], target = 2
Output: 1
Input: nums = [1,3,5,6], target = 7
Output: 4'''