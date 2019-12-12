from functools import reduce

# Lambda function with filter. Which filter out only even numbers
demo_list = [4, 2, 10, 7, 80, 85]
a = list(filter(lambda a: (a % 2 == 0), demo_list))
print(a)


# Filter using Simple function
def simple_fun(b):
    if b % 2 == 0:
        return b


x = list(filter(simple_fun, demo_list))
print(x)


# Map with Lambda function.
# Which multiply all elements and store tem into the list
a = list(map(lambda a: (a*2), demo_list))
print(a)


# Mapping using simple function
def simple_fun2(c):
    return c * 2


y = list(map(simple_fun2, demo_list))
print(y)


# Reduce using Lambda
# This will reduce the list to the sum of the all elements
sum = reduce(lambda x, y: x+y, demo_list)

print("Sum :", sum)
