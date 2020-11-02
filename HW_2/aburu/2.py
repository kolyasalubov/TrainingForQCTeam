number = input("Type 4 signs number = ")
massive = []
for i in range(len(number)):
    massive.append(number[i])
    massive[i] = int(massive[i])
print(massive[0]*massive[1]*massive[2]*massive[3])
print(number[::-1])
massive.sort()
print(massive)
