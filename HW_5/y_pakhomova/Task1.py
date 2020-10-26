#Task1
isCorrectLogin = False

while not isCorrectLogin:
    login = input("Enter your login: ")
    if login == "First":
        isCorrectLogin = True
    else:
        print("The login is incorrect! Please enter again.")

print("You have successfully logged in to your account!")
