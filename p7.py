n = 0
counter = 0


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


while(counter <= 10001):
    if(isPrime(n)):
        counter = counter + 1
    if(counter == 10001):
        print n
        break
    n = n + 1
