#Exercise 1

# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function
# to search target in nums. If target exists, then return its index. Otherwise, return -1.
# You must write an algorithm with O(log n) runtime complexity (Binary search).

def search_target(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
       mid = (left + right) // 2

       if target == nums[mid]:
           return mid
       elif target < nums[mid]:
           right = mid - 1
       else:
           left = mid + 2

    return -1


# Example 1
nums = [-1,0,3,5,9,12]
target = 9
print(search_target(nums, target))

#Example 2

nums = [-1,0,3,5,9,12]
target = 2
print(search_target(nums, target))

#Exercise 2

# Given a sorted array of distinct integers and a target value, return the index if the target is found.
# If not, return the index where it would be if it were inserted in order.
# You must write an algorithm with O(log n) runtime complexity.

def add_search (nums_1, target_1):

    low = 0
    high = len(nums_1) - 1

    while low <= high:
        mid1 = (low + high) // 2
        if target_1 == nums[mid1]:
            return mid1
        elif target_1 < nums_1[mid1]:
            high = mid1 - 1
        else:
            low = mid1 + 1
    return low


# Example 1
nums_1 = [1, 3, 5, 6]
target_1 = int(input('Please enter a number: '))
print(add_search(nums_1, target_1))



#You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your
# product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.
#Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.
#You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the
# first bad version. You should minimize the number of calls to the API.




















