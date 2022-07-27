# Squares of a sorted array

''' Given an integer array nums sorted in non-decreasing order, return an arrau of the squares of each number sorted in
 non-decreasing order.'''

# Example 1
'''
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100]
After sorting, it become [0,1,9,16,100]

'''
# Example 2
'''
Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]

'''
def solution(nums):
    return sorted(pow(i, 2) for i in nums)

nums = [-4,-1,0,3,10]
d = solution(nums)
print(d)