# *args allows us to pass numbers of arguments as mush as you want
# args stored as tuple


def sum_fun(arg1, arg2, *args):
    result = arg1 + arg2
    print("No. of extra arguments:", len(args))  # This will give the total length of extra arguments
    for element in args:
        result += element

    return result


print("Sum :", sum_fun(10, 20, 30, 40))


# **kwargs allows us to pass number of arguments as key-value pairs.
# kwargs stored as a dictionary

def mul_fun(**kwargs):
    print("kwargs:", kwargs)
    result = 1

    for key, value in kwargs.items():
        result = result * value 

    return result


print("Multiplication:", mul_fun(arg1=10, arg2=20))