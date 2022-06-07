

# doors = [False] * 101 # False represent a closed door and True for a open door we use 101 so that we can ignore the door at index 0
# print(doors)

# for i in range(1, 101):
#     doors[i] = not doors[i]
# print(doors)
#
# for i in range(1, 6):
#     for j in range(1, 4):
#         print("i:", i, "j:", j)

doors = [False] * 101 # So we can start at door no. 1 we will ignore index 0.

for i in range(1, 101):
    for j in range(i, 101, i):
        doors[j] = not doors[j]

for i in range(1, 101):
    if doors[i] is True:
        print(i, end=", ")