# Binary search

'''Remove consecutive duplcate i.e xxxxddxxx'''

def letters_filt(S: str) -> str:

    words = S[0:2]

    for i in range(2, len(S)):
        if S[i] != S[i - 1] or S[i] != S[i - 2]:
            words += S[i]
    return words
if __name__ == '__main__':
    S = input("Enter a word with consecutive characters: ")
    solution = letters_filt(S)
    print('Here is your input result: ',solution)

'''Enter a day from the list and return day + int k '''

