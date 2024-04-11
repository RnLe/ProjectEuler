from baseClass import Problem
from functools import reduce
import sys
# Problem 5

# Get number integer without leading zeros from current filename (e.g. 0001.py -> 1)
def getNumberFromFilename():
    return int(sys.argv[0].split("/")[-1].split(".")[0])


def solve():
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    def lcm(a, b):
        return a * b // gcd(a, b)
    return reduce(lcm, range(1, 21))

task = Problem(getNumberFromFilename())
task.solve(solve)