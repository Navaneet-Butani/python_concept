class Product():

    def __init__(self):
        self.__max_price = 1000

    def print_price(self):
        print("The maximum price of the computer is :{}".format(self.__max_price))

    def set_max_price(self, price):
        self.__max_price = price


computer = Product()
computer.print_price()

# Change the private variable directly
computer.__max_price = 500
# Still give previous value to the private variable
computer.print_price()


computer.set_max_price(600)
computer.print_price()
