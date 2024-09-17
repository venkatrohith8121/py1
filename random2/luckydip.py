from random  import *
lottery_nos=[]
for x in range(100):
    lottery_nos.append(randint(1000000000,9999999999))
print(lottery_nos)

luckydip=sample(lottery_nos,2)
print(luckydip)