prices=[199,99,75,65,1999,2000,4000,6000]

# by using for loop

new_prices=[]
for price in prices:
    if price>2000:
        new_prices.append(price)
print(prices)
print(new_prices)

# by using the filter 

def offer(price):
    return price>2000

filter_obj=filter(offer,prices)
new_prices=list(filter_obj)
print(prices)
print(new_prices)

# by using filter with the lambda
new_prices=list(filter(lambda price:price>2000,prices))

print(prices)
print(new_prices)