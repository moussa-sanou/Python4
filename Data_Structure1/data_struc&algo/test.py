def week_days(S: str, k: int) -> str:

    days = ['Mon','Tue', 'Wed','Thu','Fri','Sat','Sun', ]
    index = 0
    for i in range(len(days)):
        if days[i] == S:
            index = i
    return days[(index + k) % 7]
if __name__ == '__main__':
    S = input("Please Enter a day from the list: ")
    k = int(input("Enter a number: "))
    solution = week_days(S, k)
    print(solution)

