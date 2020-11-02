#module 1 
name= input ("what is your name?\n", )
print ("Ok,", name.capitalize() )
age = input ("how old are you?\n",)
print ("hmmm,", age, "it's perfect age")
city = input ('where do you live\n',)
print ("Summary:\n" , 'name =', name, "\n", 'age =', age , "\n",'city=', city.capitalize())

#module2
print ('insert some numeric variables and get result of math function')
a = float(input('set a first variable = ', ))
b = float(input('set a second variable = ', ))
def math():
    if b == 0: 
        print ('a/b = division by zero')
    else:
        print ('a/b=', a/b)
    print ('a+b =', round(a+b,5))
    print('a-b =', a-b)
    print('a*b =', a*b)
    print('a**b =', a**b)
math() 
