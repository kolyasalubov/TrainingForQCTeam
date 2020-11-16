def solution(number):
    a = []
    for i in list(range(number)):
        if i%3 == 0 or i%5 == 0:
            a.append(i)
    return sum(a)
