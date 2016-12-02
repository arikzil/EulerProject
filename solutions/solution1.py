# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9.
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.
 
def solve(upper_limit):
    numbers = get_numbers(upper_limit)
    return (numbers)


def get_numbers(numer):
    nums = 0

    for i in range(1, numer):
        if ((i % 5 == 0) or (i % 3 == 0)):
            nums += i

    return nums

# solve(1000) gives: 233168
