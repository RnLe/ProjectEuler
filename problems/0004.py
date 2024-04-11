from baseClass import Problem
import sys
# Problem 4

# Get number integer without leading zeros from current filename (e.g. 0001.py -> 1)
def getNumberFromFilename():
    return int(sys.argv[0].split("/")[-1].split(".")[0])  

def solve():
    def isPalindrome(n):
        return str(n) == str(n)[::-1]
    return max([i*j for i in range(100, 1000) for j in range(100, 1000) if isPalindrome(i*j)])


task = Problem(getNumberFromFilename())
task.solve(solve)