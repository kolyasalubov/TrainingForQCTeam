num = input("Type 4 signs number = ")
list = []
for i in range(len(num)):
    list.append(num[i])
    list[i] = int(list[i])
print(list[0]*list[1]*list[2]*list[3])
print(num[::-1])
list.sort()
print(list)