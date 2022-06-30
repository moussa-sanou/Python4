
# Given a binary array nums, return the maximum number of consecutive 1's in the array.

# Example 1:
# Input: nums = [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits two digits or the last three digits are consecutive 1s.
# The consecutive 1s is 3.

# Example 2:
# Input: nums = [1,0,1,1,0,1]
# Output: 2

# Constraints:
# 1 <= nums. length <= 10^5
# nums[i] is either 0 or 1

def findconsecutive(self, nums):
    count = 0
    max_count = 0
    for x in nums:
        if x == 1:
            count += 1
        else:
            max_count = max(max_count, count)
            count = 0
    return max(max_count, count)