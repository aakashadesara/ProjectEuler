
def rec(currentPosX, currentPosY, endX, endY):
    if(currentPosX == endX and currentPosY == endY):
        return 1
    else:
        n = 0
        if(currentPosX < endX):
            n += rec(currentPosX+1, currentPosY, endX, endY)
        if(currentPosY < endY):
            n += rec(currentPosX, currentPosY+1, endX, endY)
        print n
        return n

print rec(0,0,20,20)
