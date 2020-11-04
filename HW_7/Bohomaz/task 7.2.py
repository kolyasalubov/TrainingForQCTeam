def char_count(strn):
    dict = {}
    for i in strn:
        keys = dict.keys()
        if i in keys:
            dict[i] += 1
        else:
            dict[i] = 1
    return  dict
print(char_count(input("Enter a small text:")))
