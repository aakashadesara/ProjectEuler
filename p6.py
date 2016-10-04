N = 100

sumOfSquares = 0
squareOfSums = 0

for i in range(N+1):
    sumOfSquares = sumOfSquares + i**2
    squareOfSums = squareOfSums + i

print squareOfSums**2 - sumOfSquares
