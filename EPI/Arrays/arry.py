
'''Array are called list in python. It is a data structure that stores a collection of values where each
value is referenced using an index or a key'''

new_list = [1, 2, 3]
print(new_list)
print(new_list[1])

''' Searching in array using linear searchR'''
if 1 in new_list: print(True)

for n in new_list:
    if n == 1:
        print(True)
        break

''' Insert element in an array'''
'''Add element to a list using the append method'''
number = []
print(len(number))
number.append(2)
number.append(5)
print(number)

'''Add element using extend method'''
list1 = []
list1.extend([4,5,6])
print(list1)


