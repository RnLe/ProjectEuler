from baseClass import Problem
import sys
# Problem 6

# Get number integer without leading zeros from current filename (e.g. 0001.py -> 1)
def getNumberFromFilename():
    return int(sys.argv[0].split("/")[-1].split(".")[0])  

def solve():
    n = 100
    return sum(range(1, n+1))**2 - sum([i**2 for i in range(1, n+1)])

task = Problem(getNumberFromFilename())
task.solve(solve)