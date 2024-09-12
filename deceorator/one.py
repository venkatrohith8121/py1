def outer():
    print("outer is excetuted")
    def inner():
        print("inner")
    # print(id(inner))
    return inner
x=outer()
# print(x)
x()