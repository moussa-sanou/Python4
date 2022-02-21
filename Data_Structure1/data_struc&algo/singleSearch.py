# Linear search for non duplicate list
'''for an array named my list find the index for the x element '''

def search_x(my_list, x):
    for i in range(len(my_list)):
        if x == my_list[i]:
            print(x, "is found at index:", i)
            break
    else:
        print("Element not found in this list")

my_list = [10, 20, 80, 30, 60, 50, 110, 100, 130, 170]
x = int(input("Enter the element you want to find: "))
search_x(my_list, x)

'''In the following array you linear search to find n element'''

def find_n(Array, n):
    for i in range(len(Array)):
        if n == Array[i]:
            print(n, "is found at the index", i)
            break
    else:
        print("Not in the list")

Array = [50, 90, 30, 70, 60]
n = int(input("Enter the element needed to be found: "))

find_n(Array, n)