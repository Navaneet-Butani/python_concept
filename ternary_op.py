# Python program to demonstrate ternary operator
a, b = 10, 20

# Use tuple for selecting an item
print((b, a)[a < b])

# Use Dictionary for selecting an item
print({True: a, False: b}[a < b])

# Using Lambda
print((lambda d: b + d, lambda d: a-d)[a > b](10))