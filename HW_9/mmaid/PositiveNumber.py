class MyError(Exception): 
    def __init__(self, data): 
        self.data = data
    def __str__(self):
        return repr(self.data)

def check_positive(number):
    try:
        number = float(number)
        if number >= 1:
            return f"You input positive number: {number}"
        else:
            raise MyError(f"You input negative number: {number}. Try again.")
    except MyError as my:
        return my.data
    except:
        return "Error type: ValueError!"


