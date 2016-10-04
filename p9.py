for a in range(1000):
    for b in range(1000):
        for c in range(1000):
            if a < b and b < c and a**2 + b**2 == c**2:
                if a + b + c == 1000:
                    print str(a + b + c) + " " + str(a * b * c)
