a = int(input('Enter a number: '))
b = int(input('Enter a number: '))

number = a + b
print('a+b=',number)
number = a - b
print('a-b=',number)
number = a * b
print('a*b=',number)
if b == 0:
        print('a/b impossible devide by zero')
else:
        number = a / b
        print('a/b=',number)
number = a ** b
print('a**b=',number)

