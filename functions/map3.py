product_prices=[100,50,20,30,500,600,2000]
new_prices=[]
for price in product_prices:
    if price<1000:
        new_prices.append(price)
print(product_prices)
print(new_prices)