print('Enter four digit value:')
a = input()
a = list(a)
result = 1
for element in a:
    result = result * int(element)
print(f"Result = {result}")
a.reverse()
print(f"Reverse result = {a}")
a.sort()
print(f"Result  = {a}")


