F1 = 1
F2 = 1

i = 3
num = F1 + F2
while(len(str(num)) != 1000):
    i = i + 1
    F1 = F2
    F2 = num
    num = F1+F2
    print str(i) + " " + str(num)

print i
