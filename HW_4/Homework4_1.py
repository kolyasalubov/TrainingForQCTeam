for i in range(1, 11):
    # print(i)
    if i % 2 == 0:
        print('Even number divisible by 2 - ' + str(i))
    elif i % 2 == 1 and i % 3 == 0:
        print('Odd number divisible by 3 - ' + str(i))
    if i % 2 != 0 and i % 3 != 0:
        print('NOT divisible by 2 and 3 - ' + str(i))
