

sal_info = dict()
sal_info = {'Austin':911985, 'Dallas': 89999, 'San Jose': 100989, 'Atlanta': 89286}
print(sal_info)

if ('Dallas' in sal_info):
    print(sal_info['Dallas'])
else:
    print("Not found")

print("*****" * 20)

# Basic operations

# Modified key value
sal_info['Atlanta']= 92340
print(sal_info)

# Remove a key value pair
del sal_info['Atlanta']
print(sal_info)

# Clear a dictionary
sal_info.clear()
print(sal_info)

if ('Seattle' not in sal_info):
    sal_info['Seattle']= 110340
else:
    print("Key exists")
print(sal_info)

print("*****" * 20)

# Python Dictionary methods
sal_info = dict()
sal_info = {'Austin':911985, 'Dallas': 89999, 'San Jose': 100989, 'Atlanta': 89286}

'''Access a value from the dictionary .get(key, default message) '''
print(sal_info.get('Dallas', "not found"))
print(sal_info.get('Portland', "not found"))

''' List all keys  .keys() '''
print("*****" * 20)
print('List of all keys: ')
print(sal_info.keys())

'''List all values  .values()'''
print("*****" * 20)
print('List of all the values in the dic')
print(sal_info.values())

'''List both keys and their values .items()'''
print("*****" * 20)
print('List both keys and their values')
for k,v in sal_info.items():
    print('The key is', k, 'The value is ', v)

'''Find the maximum value in the dictionary .max()'''
print("*****" * 20)
print('Maximum value in the dic')
print('The city with the highest salary is '+ max(sal_info, key=sal_info.get))

'''Find the minimum value in the dictionary .min()'''
print("*****" * 20)
print('Minimum value in the dic')
print('The city with the lowest salary is '+ min(sal_info, key=sal_info.get))

'''Return the value associated with the key .pop(key,default)
(removes the key-value pair from dictionary)'''
print("*****" * 20)
print('Remove Key value pair')
print(sal_info)
print('value of key '+ str(sal_info.pop('Dallas', "not found")))
print(sal_info)

'''Remove last item of the dic'''
print("*****" * 20)
print('Remove the last key and value of the dic')
print(sal_info.popitem())
print(sal_info)

'''Return a sorted list  .sorted()'''
print("*****" * 20)
sal_info = {'Austin':911985, 'Dallas': 89999, 'San Jose': 100989, 'Atlanta': 89286}
print(sal_info)
print('Print the dic with sorted keys: ')
print(sorted(sal_info.keys()))
print(sorted(sal_info.values()))


'''Make a shallow copy of the dictionary  .copy()'''
print("*****" * 20)
