
'''An algorithm is a generic step by step list of instructions for solving a problem'''

# write a function which compute the sum of the first n integers

def sum_of_n(n):
    the_sum = 0
    for i in range(1, n + 1):
        the_sum = the_sum + i
    return the_sum

print(sum_of_n(10))