'''
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
'''


# gives the sum of n!
def get_num(n):
    if n == 0:
        return 1
    else:
        return n * get_num(n - 1)


# used for getting the digit sum .
def get_digit_sum(init, number):
    res = 0

    while number > 1:
        res += number % 10

        number = int(number // 10)
    return res


def solve(number):
    return get_digit_sum(0, get_num(number))


print(solve(100))
