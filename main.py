def is_even(num):
    return num % 2 == 0

def is_odd(num):
    # opposite of even
    return not is_even(num)


print(is_even(2))