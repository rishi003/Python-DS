def fib(num):
    a = 0
    b = 1
    c = a + b
    while num > 1:
        c = a + b
        a, b = b, c
        num -= 1
    return c


def rec_fib(num, memo={}):
    if num < 0:
        return "Incorrect input"
    elif num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        if memo.get(num):
            return memo.get(num)
        else:
            ans = rec_fib(num - 1, memo) + rec_fib(num - 2, memo)
            memo[num] = ans
            return ans


print(rec_fib(60))
