# Dictionary Comprehension
# Program to find dictionary of even no. keys between 1 to 10. And Square of them as values.

demo_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

new_dict = {item: item**2 for item in demo_list if (item % 2) == 0}

print(new_dict)


# Generator Comprehension
# Program to find odd no. between 1 to 100.

new_gen = (element for element in range(100) if (element % 2) != 0)
print(new_gen)

for i in new_gen:
    print(i)
