import re

while True:
    pswd = input("Enter your password ")
    if (re.search("[a-z]", pswd) and re.search("[A-Z]", pswd) and 
    re.search("\d", pswd) and re.search("[!@#$%^&*_+-=]", pswd) and
    len(pswd) >= 6 and len(pswd) <= 16):
        print("Your password is strong")
        break
    else:
        print("Your pasword is weak")
