def solution(number):
    num = 0
    for x in range(number):
        if x % 3 == 0:
            num += x
        elif x % 5 == 0:
            num += x
    return num
    