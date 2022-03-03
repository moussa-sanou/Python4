# Write a program to count number of bits that are set to 1 in a nonnegative integer

def count_bits(x: int) -> int:
    num_bits = 0
    while x:
        num_bits += x & 1
        x >>= 1
    return num_bits

# Computing the parity of a word
# How would you compute the parity of a very large number of 64-bit words
# Hint: Use a lookup table, but do not use 2**64 entries

# Brute force solution

def parity(x: int)-> int:
    result = 0
    while x:
        result ^= x & 1
        x >>= 1
    return result
