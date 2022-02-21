# Loop Through a List

'''You can loop through items by using a For loop:'''
# mylist = ['Adja', 'Mori', 'Sami']
# for x in mylist:
#     print(x)

# Loop Through the Index Numbers
'''You can also loop through a list items by referring to their 
index number'''

# mylist = ['Adja', 'Mori', 'Sami']
# for x in range(len(mylist)):
#     print(mylist[x])

# # Loop using while loop
# mylist = ['Adja', 'Mori', 'Sami']
# i = 0
# while i < len(mylist):
#     print(mylist[i])
#     i = i + 1

# Python List Comprehension
'''list comprehension offer a shorter syntax when we want to create new a list
based on the value of an existing list'''
# garba = ['attieke', 'poisson', 'piment', 'onion', 'cube magic', 'salt']
# daba = []
# for x in garba:
#     if "a" in x:
#         daba.append(x)
# print(daba)

'''let's  try the example above with list comprehension'''
# garba = ['attieke', 'poisson', 'piment', 'onion', 'cube magic', 'salt']
# daba = [x for x in garba if 'p' in x]
# print(daba)
# daba = [x for x in garba]
# print(daba)

# Python sorted list
# list = ['bondoukou', 'ouangolodougou', 'kourougouna', 'tafiere',
#         'gnakara', 'abengourou']
# list.sort()
# print(list)
# numbers = [225, 202, 1500, 8500, 3500]
# numbers.sort()
# print(numbers)

'''Sort descending'''
# list.sort(reverse = True)
# print(list)
# list.reverse()
# print(list)

'''Copy lists '''
'''use the built in python copy() method to copy a list'''
# mylist = ['Adja', 'Mori', 'Sami']
# mylist2 = mylist
# print(mylist2)
# mylist2 = mylist.copy()
# print(mylist2)

# '''join two list'''
# list1 = ['a', 'b', 'c']
# list2 = [1, 2, 3]
# list3 = list1 + list2
# print(list3)
#
# # for x in list2:
# #     list1.append(x)
# # print(list1)
#
# list1.extend(list2)
# print(list1)

'''Summary of the list method we used in this chapter'''
'copy()'
'extend()'
'sort()'
'reverse()'
'clear()'
'insert()'
'index()'
'remove()'
'append()'

# Suppose we have a list named number = [2, 6, 8, 10, 50, 70] find target = 50 and target = 1
# In number

def search(number, target, left=None, right=None):
    if left is None:
        left = 0
    if right is None:
        right = len(number) - 1
    if left > right:
        return -1
    #Find midpoint of number

    mid = (left + right) // 2
    # Start searching for target
    if target == number[mid]:
        return mid
    elif target < number[mid]:
        new_right = mid - 1
        return search(number, target, left, new_right)
    else:
        new_left = mid + 1
        return search(number, target, new_left, right)

if __name__=='__main__':
    number = [2, 6, 8, 10, 50, 70]
    target = int(input('Enter the number you want to search: '))
    solution = search(number, target)
    if solution != -1:
        print(target, 'is found at index', solution)
    else:
        print('Element not found')






