import re
def valid_email(a):
    try:
        if re.match(r"(\w+)\@[a-z]+\.[a-z]+(\.[a-z]+$|$)", a):
            return "Email is valid"
        else:
            return "Email is not valid"
    except:
        return "Email is not valid"
