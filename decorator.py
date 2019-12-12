# Program to create decorator for check division is not done by 0.

def divide_rule(func):
    def inner(a, b):
        print(a, "will going to divide by", b)
        if b == 0:
            print("This can't be divide!")
            return None
        return func(a, b)
    return inner


@divide_rule
def div(a, b):
    return a/b


print(div(10, 0))
