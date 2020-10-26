#Task2

list = [1, 3, 5, 4, 7, 8, 2]
index = 0
while index < len(list):
    list[index] = float(list[index])
    index = index + 1
print(list)
print(type(list[0]))
