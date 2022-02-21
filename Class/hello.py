# Python add list items
'''To add an item to the end of a list use the
append()'''

mylist = ['abidjan', 'bamako', 'bouake']
mylist.append('Ferkessedougou')
print(mylist)
print('-----'*20)

'''insert() is use to insert an item to a specific in a list'''
mylist.insert(0, 'Cocody')
print(mylist)
print('---'*20)

'''To merge elements of two different list we use extend()'''

loko = ['Treichville', 'abobo', 'yop']
mylist.extend(loko)
print(mylist)
print('---'*20)

# Remove list items
'''the remove () method removes a specified item from a list'''
loko = ['Treichville', 'abobo', 'yop']
loko.remove("abobo")
print(loko)
print('---'*20)

'''the pop() method removes item specified index'''
loko = ['Treichville', 'abobo', 'yop']
loko.pop(1)
print(loko)
print('---'*20)
'''if you do not specify the index pop will remove the last item'''
loko = ['Treichville', 'abobo', 'yop']
loko.pop()
print(loko)
print('---'*20)

'''del method or keyword is also to remove specified index'''
loko = ['Treichville', 'abobo', 'yop', 'mama', 'tata', 'tati', 'lol']
del loko[0:6:2]
print(loko)
print('---'*20)

'''del keyword can also delete the list completely'''
loko = ['Treichville', 'abobo', 'yop']
del loko
print('---'*20)

'''clear() is a method that empties the list'''
loko = ['Treichville', 'abobo', 'yop']
loko.clear()
print(loko)










