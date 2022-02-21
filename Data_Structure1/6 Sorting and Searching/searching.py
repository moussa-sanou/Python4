
'''Searching is the algorithm process of finding a particular item in a collection of items
A search typically answers either True or False as to wheter the item is present'''

# Sequential search

# def search_pos(a_list, pos):
#     for i in range(len(a_list)):
#         if pos == a_list[i]:
#             print(i)
#             break
#     else:
#         print('element not in list')
#
# a_list = [1, 2, 32, 8, 17, 19, 42, 13, 0]
# pos = 8
# search_pos(a_list, pos)

# Searching for duplicate elements

def search_dup(list1, pos):
    list2 = []
    dup = False
    for i in range(len(list1)):
        if pos == list1[i]:
            dup = True
            list2.append(i)

    if dup == True:
        for i in list2:
            print(i)
    else:
        print('Element not in the list')

