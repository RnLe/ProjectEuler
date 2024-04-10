from baseClass import Problem
import sys

# Get number integer without leading zeros from current filename (e.g. 0001.py -> 1)
def getNumberFromFilename():
    return int(sys.argv[0].split("/")[-1].split(".")[0])

def getPrimeFactors(n):
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n /= d
        d += 1
    return factors

def solve():
    return getPrimeFactors(600851475143)[-1]


task = Problem(getNumberFromFilename())
task.solve(solve)