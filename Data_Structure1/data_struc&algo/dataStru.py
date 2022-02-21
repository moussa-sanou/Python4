
# Linear search
'''It is a method of finding elements within a list. it is also called a sequential search . it is the simplest
searching algorithm because it searches the desired element in a sequential manner. it compares each and every element
with the value that we are searching for. '''
def lin_search (list1, x):
    for i in range(len(list1)):
        if x == list1[i]:
            print("The element", x, "is found at index", i)
            break
    else:
        print("Element not found")

list1 = [10, 20, 80, 30, 60, 50, 110, 100, 130, 170]
x = 110
lin_search(list1, x)

# If the list contains duplicate element
def lin_search (list1, x):
    list2 = []
    duplicate = False
    for i in range(len(list1)):
        if x == list1[i]:
            duplicate = True
            list2.append(i)

    if duplicate == True:
        print(x, "The x element is found at index:")
        for i in list2:
            print(i)
    else:
        print("Elements not found")

list1 = [10, 20, 80, 30, 60, 50,20, 110, 100, 130, 20, 170]
x = int(input("Enter the element needed to be found: "))
lin_search(list1, x)
print("---" * 20)



# Problem 1
'''Given an array name arr of n elements, write a function to search a given element x in arr
input : arr = [10, 20, 80, 30, 60, 50, 110, 100, 130, 170]
x = 110
output : 6 
Element x is present at index 6'''

def seach_x (arr, x ):
    for i in range(len(arr)):
        if x == arr[i]:
            print("Element found at index", i)
            break

    else:
        print("Element not in the list")

arr = [10, 20, 80, 30, 60, 50, 110, 100, 130, 170]
x = 110

seach_x(arr, x)