
'''Given a fixed integer array arr, duplicate each occurence of zero, shiffting the remaining elements to the right.
Note that elements beyond the length of the original array are not written. Do the above modifications to the input
array in place and do not return anything.'''

# Example 1
# Input: arr = [1,0,2,3,0,4,5,0]
# Output: [1,0,0,2,3,0,0,4]
'''Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]'''

# Example 2
# Input: arr = [1,2,3]
# Output: [1,2,3]
'''After calling your function, the input array is modified to [1,2,3]'''


def duplicateZeros(arr):
    i = 0
    while i < len(arr) - 1:
        if arr[i] == 0:
            arr.insert(i + 1, 0)
            arr.pop()
            i += 1
        i += 1

arr = [1,0,2,3,0,4,5,0]
print(duplicateZeros(arr))