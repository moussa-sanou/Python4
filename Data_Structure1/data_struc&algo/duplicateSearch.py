
'''duplicate item in a list'''

def myfunction(momo, x): # define a function to search for a specific element in our list.
    momo2 = []          #Create an empty list to store search items
    dup = False         # Initialize a variable that will be use to find the search item and set it as True
    for i in range(len(momo)):
        if x == momo[i]:
            dup = True
            momo2.append(i)

    if dup == True:
        print(x, "Is found at index: ")
        for i in momo2:
            print(i)
    else:
        print(x, "is not in the list")

momo = [26, 10, 90, 1, 250, 50, 310, 30, 30, 1, 1]
x = int(input("Enter the element you are looking for: "))
myfunction(momo, x)


































# def search(babi, x):                # Create a function to search for items in our list
#     duplicate = False                # Create a variable and assign True value
#     babi2 = []                      # Create an empty string to store the search items
#     for i in range(len(babi)):      # Loop through the list items to find the item x
#         if x == babi[i]:
#             duplicate = True
#             babi2.append(i)
#
#     if duplicate == True:
#         print(x, "is found at index")
#         for i in babi2:
#             print(i)
#     else:
#         print("Item not in the list")
#
#
# babi = [1, 32, 48, 2, 4, 48]
# x = int(input("Enter the element needed to be found: "))
#
# search(babi, x)

























































# Linear search for duplicate items
'''In the following list find all the indexes for duplicates'''
# def find_dup(my_list, x):
#     mylist2 = []
#     find_dup = False
#
#     for i in range(len(my_list)):
#         if x == my_list[i]:
#             find_dup = True
#             mylist2.append(i)
#
#     if find_dup == True:
#         print(x, 'is found at index')
#         for i in mylist2:
#             print(i)
#     else:
#         print("love")
#
#
# my_list = [50, 30, 60, 25, 50, 90, 50]
# x = int(input("Enter the item to be search: "))
#
# find_dup(my_list, x)