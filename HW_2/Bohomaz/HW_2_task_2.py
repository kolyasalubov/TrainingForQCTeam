num = input("enter four digits: ")
list = []
for i in range(len(num)):
    list.append(num[i])
    list[i] = int(list[i])
print(num[::-1])
list.sort()
print(list)
print(list )

# while (num != 0): 
#     mult = mult * (num % 10)
#     num = num // 10

#reverse = 0 
# while(num > 0):
#   reminder = num%10
#   reverse = (reverse *10)+reminder
#   num = num //10
# print("\n reverse of entered number is = %d" %reverse)

