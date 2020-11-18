class ToSmallNumberGroupError(Exception):
    def __init__(self, data):
        self.data = data
    def __str__(self):
        return repr(self.data)



def check_number_group(number):
    try:
        if number >= 10 and number != f"{number}":
            return f"Number of your group {number} is valid"
        else:
            raise ToSmallNumberGroupError(
        "We obtain error: Number of your group can't be less than 10")
    except ToSmallNumberGroupError as t:
        return t.data
    except:
        return "You entered incorrect data. Please try again."

