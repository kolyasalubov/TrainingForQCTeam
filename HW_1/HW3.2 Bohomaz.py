num = int (input("enter four digits: "))

mult = 1
while (num != 0): 
    mult = mult * (num % 10)
    num = num // 10
print ("product of numbers: ", mult)

#reverse = 0 
# while(num > 0):
#   reminder = num%10
#   reverse = (reverse *10)+reminder
#   num = num //10
# print("\n reverse of entered number is = %d" %reverse)
