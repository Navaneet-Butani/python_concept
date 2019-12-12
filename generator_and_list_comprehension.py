# A simple generator function
def my_gen():
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n


a = my_gen()
print(next(a))
print(next(a))
print(next(a))
# print(next(a))  # This will give error : StopIteration


# Iterate through for loop
for item in my_gen():
    print(item)



# Generator and list comprehension
# Initialize the list
my_list = [1, 3, 6, 10]

# square each term using list comprehension
# Output: [1, 9, 36, 100]
print([x**2 for x in my_list])

# same thing can be done using generator expression
# Output: generator object
a = (x**2 for x in my_list)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
