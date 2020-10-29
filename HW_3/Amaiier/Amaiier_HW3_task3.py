ran = int(input("How many Fib numbers do you want to see: = "))
fib = [0]
if ran == 0:
    print("There is no Fib numbers!")
elif ran == 1:
    print(fib)
else:
    i = 2
    fib.append(1)
    while i < ran:
        fib.append(fib[i-1]+fib[i-2])
        i = i+1
    print(fib)

