
# Reverse String

''' Write a function that reverses a string. The input string given as an array of characters s. You must do this by
modifying the input array in-place with o(1) extra memory. '''

# Example 1
''' Input: s = ['h','e','l','l','o']
 Output: ['o','l','l','e','h'] '''

# Example 2
''' Input: s = ['H','a','n','n','a','h']
Output: ['h','a','n','n','a','H'] '''

# Solution 1
def reverse_str(s):
    return s[::-1]

s = ['h','e','l','l','o']
d = reverse_str(s)
print(d)

# Solution 2
def reverse(x):
    str = ""
    for i in x:
        str = i + str
    return str
x = ['H','a','n','n','a','h']
print(reverse(x))

# Solution 1

