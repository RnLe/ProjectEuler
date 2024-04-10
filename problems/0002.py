from baseClass import Problem
import sys

# Get number integer without leading zeros from current filename (e.g. 0001.py -> 1)
def getNumberFromFilename():
    return int(sys.argv[0].split("/")[-1].split(".")[0])

# Define fibonacci generator
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def solve():
    result = 0
    for i in fibonacci():
        if i >= 4000000:
            break
        if i % 2 == 0:
            result += i
    return result


task = Problem(getNumberFromFilename())
task.solve(solve)