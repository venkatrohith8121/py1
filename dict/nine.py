numbers=[231,2342,43243,43244,4345,1412456,454367,2524358,52359,23523510]
even=0
odd=0
for number in numbers:
    if number%2==0:
        even=even+1
    elif number%2!=0:
        odd=odd+1
print(even)
print(odd)