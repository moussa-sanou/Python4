
# 278 First bad version

'''You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of
your product fails the quality check. Since each version is developed based on the previous version, all the versious
after a bad version are also bad
Suppose you have n version [1,2, .....,n] and you want to find out the first bad one, which causes all the following ones
to be bad.
You are given API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first
bad version. You should minimize the number of calls to API'''

# Example 1:
'''Input: n = 5, bad = 4
Output: 4
Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.'''

# Example 2:
'''Input: n = 1, bad = 1
Output: 1'''


# class Solution(object):
#     def firstBadVersion(self, n):
#
        # left = 1
        # right = n
        # res = 0
        # if n == 1:
        #     return 1
        # while left <= right:
        #     mid = (left + right) // 2
        #
        #     if isBadVersion(mid) is True:
        #         res = mid
        #         right = mid - 1
        #     else:
        #         left = mid + 1
        # return res

# class Solution(object):
#     def firstBadVersion(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         left = 1
#         right = n
#         while left<right:
#             mid = int((left+right)/2)
#             bol = isBadVersion(mid)
#             if(bol == False):
#                 left = mid+1
#             elif(bol == True):
#                 right = mid
#         return left