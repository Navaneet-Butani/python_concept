def outerfun(a):
    print("Outer is called")
    
    def innerfun(b):
        print("Inner is called")
        return a+b
    
    return innerfun


f = outerfun(10)
print(type(outerfun))
print(type(f))
print(f(30))

del outerfun

print(f)
