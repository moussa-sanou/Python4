

''' You are given a license key represented as string s that consists of only alphanumeric characters and dashes.
The string is seperated into n + 1 groups by n dashes. you are also given an integer K.
We want to reformat the string s such that each group contains k characters, excepts for the first group, which could
be shorter than k but still must contain at least one character. Furthermore, there must be a dash inserted between
two groups, and you should convert all lowercase letters to uppercase
Returned the reformatted license key

Example 1:
Input: s = "5F3Z-2e-9-w", k = 4
Output: "5F3Z-2E9W"
Explanation: The string s has been split into two parts, each part has 4 characters.
Note that the two extra dashes are not needed and can be removed.

Example 2:

Input: s = "2-5g-3-J", k = 2
Output: "2-5G-3J"
Explanation: The string s has been split into three parts, each part has 2 characters except the first part as it
could be shorter as mentioned above.
'''

# Since the we can have a group smaller that k in the group we will start traversing our string from right to lelft

def licensekey(s, k):
    n = len(s)
    count = 0
    ans = []
    for i in reversed(range(n)):
        if (s[i] != '-'):
            ans += s[i].upper()
            count = count + 1
            if (count == k):
                count = 0
                ans += '-'
    # we need to make sure the groups doesnt start by a dash
    if (len(ans) > 0 and ans[len(ans)-1] == '-'):
        ans = ans[:-1]
    ans = ans[::-1]
    result = "".join(ans)
    return result

s = "5F3Z-2e-9-w"
k = 4
print(licensekey(s, k))