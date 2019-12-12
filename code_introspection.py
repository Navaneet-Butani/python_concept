# type() : Which specifies typeof the object
print("Type of 'Hello':", type("Hello"))
print("Type of '10.9867':", type(10.9876))
print("Type of an object:", type(object))
print("Type of [1, 2, 3, 4, 6]:", type([1, 2, 3, 4, 6]))


# dir(): Which return list of methods and attributes
print("Dir of 'Hello!':", dir("Hello!"))
print("Dir of object", dir(object))


# id(): specifies the id regarding that object
print("ID of 'a':", id('a'))
print("ID of [1, 2, 'Hello']", id([1, 2, 'Hello']))

# repr(): Specifies representation of object
print(repr(list))

# issubclass(): Returns boolean as arg1 is subclass of arg2 then True else False
print(issubclass(list, object))

# hasattr(): Returns boolean as per 2nd arg is attribute of 1st arg or not.
list_demo = [1, 3, 5]
print(hasattr(object, 'list_demo'))
