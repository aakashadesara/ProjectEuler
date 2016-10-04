NUM = 20

def findPrimes():
    list = []
    for i in range(NUM+1):
        if(isPrime(i)):
            list += [i]
    return list

def multOfList():
    prod = 1
    for i in findPrimes():
        prod *= i
    return prod

def isPrime(j):
    if j <= 1:
        return False
    elif j <= 3:
        return True
    elif j % 2 == 0 or j % 3 == 0:
        return False
    i = 5
    while (i * i <= j):
        if j % i == 0 or j % (i + 2) == 0:
            return False
        i = i + 6
    return True


def checkDivisibility(num):
    for i in range(1,NUM+1):
        if(num % i != 0):
            return False
    return True


theSum = multOfList()
flag = True
while(flag):
    if(checkDivisibility(theSum) == True):
        print theSum
        flag = False
    else:
        theSum = theSum + multOfList()
