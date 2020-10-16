num = input("Type 4 signs number = ")
lis = []
for i in range(len(num)):
    lis.append(num[i])
    lis[i] = int(lis[i])
print(lis[0]*lis[1]*lis[2]*lis[3])
print(num[::-1])
lis.sort()
print(lis)