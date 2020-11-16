#Task3
number = int(input("Enter number: "))

previous_num = 0
current_num = 1

print(f"{previous_num},\n{current_num},")
while current_num + previous_num < number:
    temp = previous_num
    previous_num = current_num
    current_num = current_num + temp
    print(f"{current_num}, ")

