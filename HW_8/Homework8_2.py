date_dic = {1: "Monday",
            2: "Tuesday",
            3: "Wednesday",
            4: "Thursday",
            5: "Friday",
            6: "Saturday",
            7: "Sunday"}

day = input("Input number from 1 to 7:\n")

try:
    day = int(day)
    print(date_dic[day])
except (KeyError, ValueError):
    print("There should be only numbers from 1 to 7")
