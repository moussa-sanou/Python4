# Write a program to count number of bits that are set to 1 in a nonnegative integer

def count_bits(x):
    num_bits = 0
    while x:
        num_bits += x & 1
        x >>= 1
    return num_bits