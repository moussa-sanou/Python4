
# 35. Search Insert Position

'''Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return
the index if target is found. If not, return the index where it would be if it were inserted in order.
 You must write and algorithm with o(log n)'''

# Example 1:
'''Input: nums = [1,3,5,6], target = 5
Output: 2 '''

# Example 2:
'''Input: nums = [1,3,5,6], target = 2
Output: 1 '''

# Example 3:
'''Input: nums = [1,3,5,6], target = 7'''

class Solution(object):
    def searchInsert(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return left