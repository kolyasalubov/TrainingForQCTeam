date_dic = {1: "Sunday",
    2: "Monday",
    3: "Tuesday",
    4: "Wednesday",
    5: "Thursday",
    6: "Friday",
    7: "Satuday"}

day = input("Input number: ")

try:
    day = int(day)
    print(date_dic[day])
except KeyError:
    print("Number should be from 1 to 7")
except ValueError:
    print("Number should be numeric")
