NUM = 100

def factorial(x):
    if(x == 0):
        return 1
    else:
        return x * factorial(x-1)

sum = 0
for i in range(len(str(factorial(NUM)))):
    sum += int(str(factorial(NUM))[i])

print sum
