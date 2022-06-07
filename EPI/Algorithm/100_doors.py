

doors = [False] * 101 # False represent a closed door and True for a open door we use 101 so that we can ignore the door at index 0
print(doors)

for i in range(1, 101):
    doors[i] = not doors[i]
print(doors)

for i in range(1, 6):
    for j in range(1, 4):
        print("i:", i, "j:", j)