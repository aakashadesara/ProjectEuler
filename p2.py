a = 0
b = 1
sum = a + b

totalSum = 0

while(sum < 4000000):
    if(b % 2 == 0):
        totalSum += b

    sum = a+b
    a = b
    b = sum

print totalSum
