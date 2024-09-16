def divide_check(func):
    def inner(a,b):
        if b==0:
            print("cant be divisible by zero")
        else:
            return func(a,b)
    return inner

@divide_check
def divide(a,b):
    print(a/b)
divide(10,2)
divide(10,0)