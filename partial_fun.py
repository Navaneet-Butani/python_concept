# Partial function

from functools import partial


# In this we create number of four digit.
def digit_fun(no1, no2, no3, no4):
    number = (1000*no1) + (100*no2) + (10*no3) + no4
    return number


partial_fun = partial(digit_fun, 5, 4)

print("Four digit no:", partial_fun(3, 2))
