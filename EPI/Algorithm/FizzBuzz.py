
# Fizz Buzz
'''Fizz buzz is a game for two or more players
Take it in turns to count aloud from 1 to 100, but each time you are going to say a multiple of 3,
replace it with the word fizz
For multiple of 5 , say buzz and for numbers that are multiples of both 3 and 5, say fizz, buzz'''

for i in range(1, 101):

    if i % 3 == 0 and i % 5 == 0:
         print('fizzbuzz')

    if i % 3 == 0:
        print("fizz")

    elif i % 5 == 0:
        print('buzz')

    else:
        print(i)