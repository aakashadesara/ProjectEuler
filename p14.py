
def countNum(num):
    startingN = num
    count = 1

    while(startingN != 1):
        if(startingN % 2 == 0):
            startingN = startingN / 2
        elif(startingN % 2 == 1):
            startingN = startingN * 3 + 1
        count += 1

    return count

maxCount = 0
location = 0
for i in range(1,1000000):
    if(maxCount < countNum(i)):
        print str(maxCount) + " " + str(location)
        maxCount = countNum(i)
        location = i

print str(maxCount) + " " + str(location)
