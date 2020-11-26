import re
password = input('Enter password:\n')
if re.search('[a-z]', password) and re.search('[A-Z]', password) and re.search('[0-9]', password)\
        and re.search('[@#$]', password) and len(password) >= 6 <= 16:
    print('Valid password')
else:
    print('Use a-z, A-Z, 0-9 and $ # @ in your password')
