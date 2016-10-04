high = 0


def isPalindrome(sum):
    if(len(str(sum)) == 5):
        if str(sum)[0] == str(sum)[4] and str(sum)[1] == str(sum)[3]:
            return True
    elif(len(str(sum)) == 6):
        if str(sum)[0] == str(sum)[5] and str(sum)[1] == str(sum)[4] and str(sum)[2] == str(sum)[3]:
            return True
    return False;


for j in range(100,1000):
    for i in range(100, 1000):
        if(isPalindrome(i*j) and i*j>high):
            high = i*j

print high
