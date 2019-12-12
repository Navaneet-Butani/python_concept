class Student:

    def __init__(self, name, id, age):
        self.name = name
        self.id = id
        self.age = age

    def display_details(self):  
        print("Name:%s, ID:%d, age:%d" % (self.name, self.id))


s = Student("John", 101, 22)
print("__doc__:", s.__doc__)

print("__dict__:", s.__dict__)

print("__module__:", s.__module__)
