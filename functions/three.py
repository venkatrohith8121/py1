numbers=[10,20,30,40]
# new_number=[]
# for num in numbers:
#     new_number.append(num*num)

# print(new_number)


# by using mapp

# def squarit(num):
#     return num*num

# new_number=list(map(squarit,numbers))

# print(new_number)


# by using  map and lambda
new_number=list(map(lambda num:num*num,numbers))
print(new_number)

map