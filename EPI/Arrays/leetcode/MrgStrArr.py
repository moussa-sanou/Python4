
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

def merge(nums1, nums2):
    for i in nums1 and nums2:
        if i == 0:
            return nums1.remove(i)
        else:
            nums3 = nums1 + nums2
            solu = sorted(nums3)
            return solu




nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
res = merge(nums1, nums2)
print(res)