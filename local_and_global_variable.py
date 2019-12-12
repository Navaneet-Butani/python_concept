# Global Variable
global x 
x = 10
print("global x on top: "+str(x))


def print_fun():
    # Local Variable
    global x
    x = 20
    print("x in function : "+str(x))


print("Outside method before calling function x :" + str(x))

print_fun()

print("Afer calling fun " + str(x))
