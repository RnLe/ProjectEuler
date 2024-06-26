from baseClass import Problem
import sys

# Get number integer without leading zeros from current filename (e.g. 0001.py -> 1)
def getNumberFromFilename():
    return int(sys.argv[0].split("/")[-1].split(".")[0])

def solve():
    # Brute force solution
    result = 0
    for i in range(1000):
        if i % 3 == 0 or i % 5 == 0:
            result += i
    return result


task = Problem(getNumberFromFilename())
task.solve(solve)