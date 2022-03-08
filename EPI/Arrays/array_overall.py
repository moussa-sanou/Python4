
'''Max Consecutive Ones'''

# Given a binary array nums, return the maximum number of consecutive 1's in the array.
# Example 1
# Input: nums = [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s. The maximum of consecutive 1s is 3.
# Example 2
# Input: nums = [1,0,1,1,0,1]
# Output: 2

class Solution():
    def findMaxConse(self, nums):
        count = 0
        max_count = 0
        for i in nums:
            if i == 1:
                count += 1
            else:
                max_count = max(count, max_count)
                count = 0
        return max(max_count, count)

# def main():
#     nums = [1, 1, 0, 1, 1, 1]
#     task = Solution()
#     task.findMaxConse(nums)

# if __name__=='__main__':
#     main()

nums = [1,0,1,1,0,1]
task = Solution()
task.findMaxConse(nums)
print(task.findMaxConse(nums))