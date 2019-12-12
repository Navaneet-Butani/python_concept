class Shape:
    def __init__(self):
        print("This is Shape class")
    
    def area(self):
        print("Area of the Shape")


class Circle(Shape):
    def __init__(self):
        print("This is Circle class")

    # Overload the method
    # It can't be access
    def area(self, rad):
        print("Area of the Circle")

    # Override the method
    # This only be recognised
    def area(self, rad):
        print("Area : "+str(3.14*rad*rad))


s = Shape()
c = Circle()

c.area(10)

# Will give error : TypeError
# Because we define another method with same name and one parameter hence this will be replaced by that one
c.area()    
