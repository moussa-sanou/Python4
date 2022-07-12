
'''You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing
the number of elements in nums1 and nums2 respectively.
Merge nums1 and nums 2 into a single array sorted in non-decreasing order.
The final sorted array should not be returned by the function, but instead be sorted inside the array nums1. To
accomodate this, nums1 has a lenght of m + n, where the first m elements denote the elements that should be merged, and
last n elements set to 0 and should be ignored. nums has a lenght of n'''

# Example 1:
# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].

# Example 2:
# Input: nums1 = [1], m = 1, nums2 = [0], n = 0
# Output: [1]

# Example 2:
# Input: nums1 = [0], m = 0, nums2 = [1], n = 1
# Output: [1]

class Solution(object):
    def merge(self, nums1, m, nums2, n):

        # Make a copy of the first m elements of nums1
        nums1_copy = nums1[:m]

        # Read pointers for nums1copy and nums2
        p1 = 0
        p2 = 0

        # Compare elements from nums1copy and nums2 and write the smallest to nums1.

        for p in range(n + m):
            # We also need to ensure that p1 and p2 aren't over the boundaries of their respective arrays.
            if p2 >= n or (p1 < m and nums1_copy[p1] <= nums2[p2]):
                nums1[p] = nums1_copy[p1]
                p1 += 1
            else:
                nums1[p] = nums2[p2]
                p2 += 1



nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
m = 3
n = 3


res = Solution()
res.merge(nums1, m, nums2, n)
print(res.merge(nums1, m, nums2, n))

#
# class Solution(object):
#     def search(self, nums, target):
#         left = 0
#         right = len(nums) - 1
#
#         while left <= right:
#             mid = (left + right) // 2
#             if nums[mid] == target:
#                 return mid
#             elif target < nums[mid]:
#                 right = mid - 1
#             else:
#                 left = mid + 1
#         return -1



