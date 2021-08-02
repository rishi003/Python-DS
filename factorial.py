def factorial(num):
    if num == 0:
        return 1
    return num * factorial(num - 1)


def loop_factorial(num):
    res = 1
    while num > 0:
        res *= num
        num -= 1
    return res


print(factorial(4), loop_factorial(4))
