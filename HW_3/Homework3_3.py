print("Enter number")
n = input()
n = int(n)
fib = [0, 1]
for i in range(n):
    next_element = (fib[i] + fib[i - 1])
    if next_element > n:
        break
    if i == 0:
        continue
    fib.append(next_element)
print(fib)