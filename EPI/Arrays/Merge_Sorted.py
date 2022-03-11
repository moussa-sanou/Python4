
''' Merge Sorted Array '''

# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integer m and n, responding
# The number of elements in nums1 and nums2 respectively.
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.
# The final sorted array should not be returned by the function, but instead be sorted inside the array nums1.
# To accommodate this, nums has a length of m + n, where the first m elements denote the elements that should be merge,
# and the last n elements are the set to 0 and should be ignored. nums2 has a length of n.

# Example 1:
# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6]. The result of the merge is [1,2,2,3,5,6] with the
# underlined elements coming from nums1

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        newlist = sorted(nums1.extend(nums2))
        return newlist


nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
list1 = Solution()
list1.merge()