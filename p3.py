NUM = 1000000


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

def findPrimes():
    list = []
    for i in range(NUM+1):
        if(isPrime(i)):
            list += [i]
    return list

print len(findPrimes())
