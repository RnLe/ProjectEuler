from baseClass import Problem
import sys
# Problem 7

# Get number integer without leading zeros from current filename (e.g. 0001.py -> 1)
def getNumberFromFilename():
    return int(sys.argv[0].split("/")[-1].split(".")[0])  

def solve():
    def isPrime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True
    n = 10001
    i = 2
    count = 0
    while True:
        if isPrime(i):
            count += 1
        if count == n:
            return i
        i += 1

task = Problem(getNumberFromFilename())
task.solve(solve)