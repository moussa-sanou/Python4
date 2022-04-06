

# A hash table goal is to keep the data evenly distributed across the table, at least one-third empty
# A hash table amounts to a combination of two things with which we're quite familiar
'''First, a hash function, which returns a nonnegative integer value called a hash code.
Second,an array capable of storing data of type we wish to place into the data structure.'''

print(hash(3.14))
print(hash(3.14159265358979323846264338327950288419716939937510))
print(hash("Lorem"))
print(hash("Lorem ipsum dolor sit amet, consectetur adipisicing elit,"
 "sed do eiusmod tempor incididunt ut labore et dolore magna"
"aliqua. Ut enim ad minim veniam, quis nostrud exercitation"
"ullamco laboris nisi ut aliquip ex ea commodo consequat."
"Duis aute irure dolor in reprehenderit in voluptate velit"
"esse cillum dolore eu fugiat nulla pariatur. Excepteur sint"
"occaecat cupidatat non proident, sunt in culpa qui officia"
"deserunt mollit anim id est laborum."))

print(hash(None))
print(hash(hash))

class hashtest:
    pass

print(hash(hashtest))