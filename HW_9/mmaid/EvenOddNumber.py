def check_odd_even(a):
    try:
        if a%2 == 0:
            return "Entered number is even"
        else:
            return "Entered number is odd"
    except:
        return "You entered not a number."
