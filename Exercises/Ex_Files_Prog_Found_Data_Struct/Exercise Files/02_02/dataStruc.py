# Data structure are type of container capable of organizing, storing and accessing data

# String is a sequence of character

# There are two categories of data type

# 1/ Referenced types: Strings and Data structure
# 2/ Primitive types: in boolean float ...

# Arrays: It is a collection of elements, where each item is identified by an index or key
# Data Structure: it is a collection with a defined way of accessing and storing items.

StudentPetCount = [0, 1, 0, 2, 1, 1, 4, 0, 0, 0, 3, 2, 1, 3, 0, 2, 2, 4]

print(len(StudentPetCount))
print(StudentPetCount[3])

sum = 0

for x in StudentPetCount:
    sum = sum + x
print(sum)

dinnerChoices = [["Salada", "Soup", "Cheese Plate"], ["Chicken", "Salmon", "Lasagna"]]
print(dinnerChoices[1][0])
print(dinnerChoices[0][1])

