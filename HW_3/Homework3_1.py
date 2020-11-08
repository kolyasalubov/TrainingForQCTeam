print('Enter four digit value:')
a = input()
a = list(a)
fact = 1
for element in a:
    fact = fact * int(element)
print(f"Factorial {fact}")